from twilio.rest import TwilioRestClient

# put your own credentials here
s = "ACa9c9ef8d8aff695a74767ed286eea836"
t = "b08b6b2ac5a656df60c4a7af7a2bc7c7"

c = TwilioRestClient(s, t)

tn = "+13093978751"
fn = "+17656334755"

ua = "http://devpostcommit.s3.amazonaws.com/TEST/1mb_5s.mp4"
ba = "Today on WTF: a 1mb / 5s video. (anything larger won't work)"

ub = "http://devpostcommit.s3.amazonaws.com/TEST/2mb_14s.mp4"
bb = "Today on WTF: a 2mb / 14s video."

uc = "http://devpostcommit.s3.amazonaws.com/TEST/5mb_30s.mp4"
bc = "Today on WTF: a 5mb / 30s video."

c.messages.create(
    to=tn,
    from_=fn,
    body= ba + " Msg STOP to unsubscribe. Join the discussion @ http://foo.bar/sdfs",
    media_url=ua,
)
