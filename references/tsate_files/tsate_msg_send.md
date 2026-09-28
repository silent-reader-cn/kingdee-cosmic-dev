# 消息发送-tsate_msg_send

## 消息发送-主表 t_tsate_msg_send

- **表名称：** 消息发送-主表
- **表名：** t_tsate_msg_send

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fnodetype | 接收系统 | varchar | 30 |  | √ | ' ' | 接收系统,枚举: |
| 3 | freqcontent_tag | 请求内容_详情 | text | 0 |  |  | null | 请求内容_详情 |
| 4 | ferrormsg | 错误原因 | varchar | 2000 |  | √ | ' ' | 错误原因 |
| 5 | fdealtimes | 处理次数 | int8 | 64 |  | √ | 0 | 处理次数 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | frespcontent_tag | 响应内容_详情 | text | 0 |  |  | null | 响应内容_详情 |
| 8 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: zzsybnsr :增值税一般纳税人 zzsxgmnsr :增值税小规模纳税人 qysdsjb :企业所得税季报 qysdsnb :企业所得税年报 fjsf :附加税费 |
| 9 | fmsgtype | 消息类型 | varchar | 30 |  | √ | ' ' | 消息类型,枚举: |
| 10 | freqcontent | 请求内容 | varchar | 2000 |  | √ | ' ' | 请求内容 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: waiting :待处理 fail :失败 success :成功 : : : : |
| 13 | fbusinessid | 业务id | varchar | 200 |  | √ | ' ' | 业务id |
| 14 | frespcontent | 响应内容 | varchar | 2000 |  | √ | ' ' | 响应内容 |
| 15 | frequrl | 请求url | varchar | 600 |  | √ | ' ' | 请求url |
| 16 | fglpzhm | 关联凭证号 | varchar | 50 |  | √ | ' ' | 关联凭证号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_msg_send |  | fbusinessid,fbusinesstype |
| 2 | pk_tsate_msg_send |  | fid |
