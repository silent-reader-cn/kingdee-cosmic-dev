# 项目扩展参数-src_extendparam

## 项目扩展参数-主表 t_src_extendparam

- **表名称：** 项目扩展参数-主表
- **表名：** t_src_extendparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fparamvalue | 参数值 | varchar | 510 |  | √ | ' ' | 参数值 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fparameterid | 参数编码 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_extendparam_param |  | fparameterid |
| 2 | idx_src_extendparam_pid |  | fprojectid |
| 3 | pk_src_extendparam |  | fid |
