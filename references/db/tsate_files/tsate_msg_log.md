# 税企日志-tsate_msg_log

## 税企日志-主表 t_tsate_msg_log

- **表名称：** 税企日志-主表
- **表名：** t_tsate_msg_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 操作说明 | varchar | 100 |  | √ | ' ' | 操作说明 |
| 3 | fsrcsys | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: taxc :税务云 |
| 4 | fnodetype | 所属系统 | varchar | 30 |  | √ | ' ' | 所属系统,枚举: 1 :税局申报 |
| 5 | freqcontent_tag | 提交内容_详情 | text | 0 |  |  | null | 提交内容_详情 |
| 6 | fcreaterld | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fmsgtype | 日志类型 | varchar | 30 |  | √ | ' ' | 日志类型,枚举: 1 :增值税申报 2 :企业所得税申报 |
| 9 | freqcontent | 提交内容 | varchar | 510 |  | √ | ' ' | 提交内容 |
| 10 | fstatus | 操作状态 | varchar | 30 |  | √ | ' ' | 操作状态,枚举: 1 :成功 0 :失败 |
| 11 | fbusinessid | 业务id | varchar | 200 |  | √ | ' ' | 业务id |
| 12 | ftarsys | ftarsys | varchar | 100 |  | √ | ' ' |  |
| 13 | fperiod | 税期 | timestamp | 0 |  |  | null | 税期 |
| 14 | fnodeid | 目标系统 | varchar | 30 |  | √ | ' ' | 目标系统,枚举: sz :深圳 qd :青岛 |
| 15 | forgname | 组织名称 | varchar | 100 |  | √ | ' ' | 组织名称 |
| 16 | flogtype | flogtype | varchar | 100 |  | √ | ' ' |  |
| 17 | frequrl | 请求地址 | varchar | 100 |  | √ | ' ' | 请求地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tsate_msg_log |  | forgname,fperiod |
| 2 | pk_tsate_msg_log |  | fid |
