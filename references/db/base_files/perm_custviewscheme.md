# 业务视图方案配置属性-perm_custviewscheme

## 业务视图方案配置属性-主表 t_perm_custviewscheme

- **表名称：** 业务视图方案配置属性-主表
- **表名：** t_perm_custviewscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentitynum | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | fviewscheme | 视图方案 | int8 | 64 |  | √ | 0 | [组织视图方案 bos_org_viewschema](../base_files/bos_org_viewschema.md) |
| 4 | forgfunc | 组织职能 | int8 | 64 |  | √ | 0 | [组织职能类型 bos_org_biz](../base_files/bos_org_biz.md) |
| 5 | fappid | 应用 | varchar | 18 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_custviewscheme |  | fappid,fentitynum |
| 2 | t_perm_custviewscheme_pkey |  | fid |
