# 权限追加升级登记-xkperm_permitem_append

## 权限追加升级登记-主表 t_xkperm_permitem_append

- **表名称：** 权限追加升级登记-主表
- **表名：** t_xkperm_permitem_append

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisok | 是否已升级 | bpchar | 1 |  |  | ' ' | 是否已升级 |
| 3 | flog_tag | 升级日志_详情 | text | 0 |  |  | null | 升级日志_详情 |
| 4 | fsappid | 原应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 5 | flog | 升级日志 | varchar | 256 |  |  | ' ' | 升级日志 |
| 6 | fappenddate | 升级日期 | timestamp | 0 |  |  | null | 升级日期 |
| 7 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | ftentityid | 追加业务对象 | varchar | 36 |  |  | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 9 | fcreater | 创建人 | varchar | 36 |  |  | ' ' | 创建人 |
| 10 | ftappid | 追加应用 | varchar | 36 |  |  | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 11 | fspermitemid | 原权限项 | varchar | 36 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 12 | ftpermitemid | 追加权限项 | varchar | 36 |  |  | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 13 | fsentityid | 原业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_permitem_append |  | fid |
| 2 | idx_xkperm_permitem_append |  | fisok,fappenddate |
