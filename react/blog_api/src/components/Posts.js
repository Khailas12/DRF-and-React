import React from 'react';
import { makeStyles } from '@material-ui/core/Styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';
import Container from '@material-ui/core/Container';


const useStyles = makeStyles((theme) => ({
	cardMedia: {
		paddingTop: '56.25%', // 16:9
	},
	
	link: {
		margin: theme.spacing(1, 1.5),
	},

	cardHeader: {
		backgroundColor:
			theme.palette.type === 'light'
				? theme.palette.grey[200]
				: theme.palette.grey[700],
	},

	postTitle: {
		fontSize: '16px',
		textAlign: 'left',
	},

	postText: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '12px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
}));


const Posts = (props) => {
	const { posts } = props;
	const classes = useStyles();
	
	if (!posts || posts.length === 0) 
	return (
		<p>
			Can't Find any Posts at the moment
		</p>
	);

	return (
		<React.Fragment>
			<Container maxWidth='md' component='main'>
				<Grid container spacing={5} alignItems='flex-end'>
					
					{posts.map((post) => {
						return (
							<Grid item key={post.id} xs={12} md={4}>

								<Card classes={classes.card}>
									<Link 
										color='textPrimary'
										href={'post/' + post.slug}
										className={classes.link}
									>
										<CardMedia
											className={classes.cardMedia}
											image='https://source.unsplash.com/random'
											title='Image title'
										/>
									</Link>

									<CardContent className={classes.CardContent}>
										<Typography
											gutterBottom
											variant='h6'
											className={classes.postTitle}
										>
											{post.title.substr(0, 50)}...
										
										</Typography>

									<div className={classes.postText}>
										<Typography color='textSecondary'>
											{post.excerpt.substr(0, 40)}
										</Typography>
									</div>

									</CardContent>
								</Card>

							</Grid>
						);
					})}
				</Grid>
			</Container>
		</React.Fragment>

	);
};

export default Posts;