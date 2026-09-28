# 跟进任务流程-didc_taskprogresspage

## 跟进任务流程-主表 t_didc_taskprogress

- **表名称：** 跟进任务流程-主表
- **表名：** t_didc_taskprogress

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 用户信息 bos_usergroup_user |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 审核日期 |
| 7 | fprogress_value | 进度 | numeric | 23 | 10 | √ | 0 | 进度 |
| 8 | ftransfer | 转交人id | int8 | 64 |  | √ | 0 | 用户信息 bos_usergroup_user |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 10 | fcreatedate | 时间 | varchar | 50 |  | √ | ' ' | 时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fprogress_message_tag | 留言_详情 | text | 0 |  |  | ' ' | 留言_详情 |
| 13 | fprogress_message | 留言 | varchar | 255 |  | √ | ' ' | 留言 |
| 14 | fdealmethod | 处理方式 | varchar | 50 |  | √ | ' ' | 处理方式 |
| 15 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 16 | fnotice | 并 | varchar | 50 |  | √ | ' ' | 并,枚举: 1 :发送通知 2 :不发送通知 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fchannel | 消息渠道 | varchar | 255 |  | √ | ' ' | 消息渠道,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_taskprogress |  | fbillno |
| 2 | pk_t_didc_taskprogress |  | fid |
