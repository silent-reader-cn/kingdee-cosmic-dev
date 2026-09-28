# 消息记录表-plm_mqmessage

## 消息记录表-主表 t_plmsm_mqmessages

- **表名称：** 消息记录表-主表
- **表名：** t_plmsm_mqmessages

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftypeflag | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 3 | fstatusname | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 1 :新建 2 :处理中 3 :成功 4 :失败 |
| 4 | fstatus | 状态 | int4 | 32 |  | √ | 1 | 状态 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fsucceednumber | 成功处理条数 | int4 | 32 |  | √ | 0 | 成功处理条数 |
| 9 | ffailmessage | 失败消息 | varchar | 1024 |  | √ | ' ' | 失败消息 |
| 10 | fcreatetime | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 11 | fdesc | 描述 | varchar | 256 |  | √ | ' ' | 描述 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_mqmessages |  | fid |
| 2 | idx_t_plmsm_mqmessages |  | ftype,ftypeflag |
