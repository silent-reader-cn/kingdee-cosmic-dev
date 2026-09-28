# 消息表开始表-plm_mqmessage_start

## 消息表开始表-主表 t_plmsm_mqmessage_start

- **表名称：** 消息表开始表-主表
- **表名：** t_plmsm_mqmessage_start

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 5 | fmodifytime | 修改日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmsm_mqmessage_start |  | fcreatorid |
| 2 | pk_t_plmsm_mqmessage_start |  | fid |
