# 轻应用集成平台连接配置-bos_thirdapps_config

## 轻应用集成平台连接配置-主表 t_bas_thirdapps_config

- **表名称：** 轻应用集成平台连接配置-主表
- **表名：** t_bas_thirdapps_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fcorpid | 企业团队ID | varchar | 50 |  | √ | ' ' | 企业团队ID |
| 7 | fxknlpstatus | NLP初始化状态 | varchar | 50 |  | √ | ' ' | NLP初始化状态,枚举: 1 :是 0 :否 |
| 8 | fcorpname | 企业团队名称 | varchar | 50 |  | √ | ' ' | 企业团队名称 |
| 9 | fthirdapptype | 平台类型 | int8 | 64 |  | √ | 0 | [移动平台类型 bas_instantmsgtype](../base_files/bas_instantmsgtype.md) |
| 10 | fdata | 数据 | varchar | 2000 |  | √ | ' ' | 数据 |
| 11 | fcorpsecret | 企业团队密钥 | varchar | 256 |  | √ | ' ' | 企业团队密钥 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_thirdapps_corpid |  | fcorpid |
| 2 | pk_bas_thirdapps_config |  | fid |
