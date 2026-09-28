# 用户默认系统首页列表-portal_scheme_user_rel

## 用户默认系统首页列表-主表 t_bas_usermainpage

- **表名称：** 用户默认系统首页列表-主表
- **表名：** t_bas_usermainpage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fschemeid | 方案 | int8 | 64 |  | √ | 0 | 首页方案 portal_scheme |
| 3 | fuserid | 人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_usermainpage |  | fid |
| 2 | idx_t_bas_usermainpage_user |  | fuserid |
