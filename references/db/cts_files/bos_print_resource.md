# 打印资源文件-bos_print_resource

## 打印资源文件-主表 t_svc_printresource

- **表名称：** 打印资源文件-主表
- **表名：** t_svc_printresource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | filetype | 文件类型 | varchar | 20 |  | √ | ' ' | 文件类型 |
| 3 | filename | 文件名 | varchar | 120 |  | √ | ' ' | 文件名 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | ftype | 资源类型 | bpchar | 1 |  | √ | ' ' | 资源类型,枚举: 0 :图片 1 :图标 2 :附件 3 :字体 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 7 | fprinttplid | 所属实体ID | varchar | 36 |  | √ | ' ' | 所属实体ID |
| 8 | furl | 文件地址 | varchar | 300 |  | √ | ' ' | 文件地址 |
| 9 | filesize | 文件大小 | int8 | 64 |  | √ | 0 | 文件大小 |
| 10 | fpowerscope | 权限范围 | bpchar | 1 |  | √ | ' ' | 权限范围,枚举: 0 :公共资源 1 :内部资源 2 :当前用户 3 :当前组织 4 :当前租户 |
| 11 | fdata | fdata | bytea | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_svc_printresource_n |  | fprinttplid |
| 2 | pk_t_svc_printresource |  | fid |
