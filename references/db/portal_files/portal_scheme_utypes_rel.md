# 方案与人员类型关系-portal_scheme_utypes_rel

## 方案与人员类型关系-主表 t_bas_usertypesmainpage

- **表名称：** 方案与人员类型关系-主表
- **表名：** t_bas_usertypesmainpage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fschemeid | 方案 | int8 | 64 |  | √ | 0 | 首页方案 portal_scheme |
| 3 | fusertypeid | 人员类型 | int8 | 64 |  | √ | 0 | 人员类型 bos_usertype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_utype_fschemeid |  | fschemeid |
| 2 | pk_bas_usertypesmainpage |  | fid |
| 3 | idx_utypesmainpage |  | fusertypeid |
