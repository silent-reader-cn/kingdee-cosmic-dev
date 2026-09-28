# 单据集成通知-isc_dc_bill_notify

## 单据集成通知-主表 t_isc_dc_bill_notify

- **表名称：** 单据集成通知-主表
- **表名：** t_isc_dc_bill_notify

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmsg_content | 消息内容 | varchar | 1000 |  | √ | ' ' | 消息内容 |
| 3 | fname | 消息推送名称 | varchar | 100 |  | √ | ' ' | 消息推送名称 |
| 4 | fperson | 苍穹用户 | varchar | 1000 |  | √ | ' ' | 苍穹用户 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | foutsideperson_var | 接收人变量-非苍穹用户 | varchar | 1000 |  | √ | ' ' | 接收人变量-非苍穹用户 |
| 7 | foutsideperson | 非苍穹用户 | varchar | 1000 |  | √ | ' ' | 非苍穹用户 |
| 8 | fmaxmsgnum | 发送次数阈值 | int4 | 32 |  | √ | 0 | 发送次数阈值 |
| 9 | fmsg_title | 消息标题 | varchar | 50 |  | √ | ' ' | 消息标题 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstate | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fnotifytype | 消息渠道 | varchar | 100 |  | √ | ' ' | 消息渠道,枚举: |
| 14 | ftrigger | 启动方案 | int8 | 64 |  | √ | 0 | [启动方案 isc_data_copy_trigger](../iscb_files/isc_data_copy_trigger.md) |
| 15 | fcondition | 发送条件 | varchar | 50 |  | √ | ' ' | 发送条件,枚举: success :单据集成成功 failed :单据集成失败 |
| 16 | fposition | 苍穹岗位 | varchar | 1000 |  | √ | ' ' | 苍穹岗位 |
| 17 | fnumber | 消息推送编码 | varchar | 100 |  | √ | ' ' | 消息推送编码 |
| 18 | fperson_var | 接收人变量-苍穹用户 | varchar | 1000 |  | √ | ' ' | 接收人变量-苍穹用户 |
| 19 | fchannel | 消息渠道（旧） | varchar | 50 |  | √ | ' ' | 消息渠道（旧）,枚举: 1 :系统消息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_dc_bill_notify_1 |  | ftrigger |
| 2 | pk_t_isc_dc_bill_notify |  | fid |
