# 智能招聘配置字典-recru_param

## 智能招聘配置字典-主表 t_recru_cfgparam

- **表名称：** 智能招聘配置字典-主表
- **表名：** t_recru_cfgparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 3 | fvalue | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fnumber | 参数编码 | varchar | 60 |  | √ | ' ' | 参数编码 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_cfgparam_fname |  | fname |
| 2 | idx_recru_cfgparam_fnumber |  | fnumber |
| 3 | pk_recru_cfgparam |  | fid |
