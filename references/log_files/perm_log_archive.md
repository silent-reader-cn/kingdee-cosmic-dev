# 权限日志归档-perm_log_archive

## 权限日志归档-主表 t_perm_log_archive

- **表名称：** 权限日志归档-主表
- **表名：** t_perm_log_archive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finterface_method | 接口方法 | varchar | 100 |  | √ | ' ' | 接口方法 |
| 3 | fhas_gendiff | 是否已生成差异 | bpchar | 1 |  | √ | '0' | 是否已生成差异 |
| 4 | fbusi_type | 业务类型 | varchar | 100 |  | √ | ' ' | 业务类型 |
| 5 | fop | 操作标识 | varchar | 100 |  | √ | ' ' | 操作标识 |
| 6 | fcloud_id | 云 | varchar | 36 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 7 | foper_name | 操作用户名称 | varchar | 50 |  | √ | ' ' | 操作用户名称 |
| 8 | fperm_item_name | 权限项名 | varchar | 50 |  | √ | ' ' | 权限项名 |
| 9 | ffiling_time | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 10 | fdiff_content | 差异内容 | text | 0 |  |  | null | 差异内容 |
| 11 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 12 | fafter_data | 操作后数据 | text | 0 |  |  | null | 操作后数据 |
| 13 | fop_item_id | 操作项ID | varchar | 100 |  | √ | ' ' | 操作项ID |
| 14 | foper_number | 操作用户工号 | varchar | 36 |  | √ | ' ' | 操作用户工号 |
| 15 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fop_item_name | 操作项名称 | varchar | 100 |  | √ | ' ' | 操作项名称 |
| 17 | fop_desc | 操作描述 | text | 0 |  |  | null | 操作描述 |
| 18 | fform_name | 表单名称 | varchar | 200 |  | √ | ' ' | 表单名称 |
| 19 | foper_username | 操作用户用户名 | varchar | 255 |  | √ | ' ' | 操作用户用户名 |
| 20 | foper_org_name | 操作组织名 | varchar | 50 |  | √ | ' ' | 操作组织名 |
| 21 | fclient_type | 客户端类型 | varchar | 300 |  | √ | ' ' | 客户端类型,枚举: web :PC端 mobile :移动端 api :接口 |
| 22 | fcloud_name | 云名称 | varchar | 100 |  | √ | ' ' | 云名称 |
| 23 | foper_id | 操作用户ID | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | foper_org_id | 操作组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fopbtn | 操作按钮名称 | varchar | 100 |  | √ | ' ' | 操作按钮名称 |
| 26 | fop_item_number | 操作项编码 | varchar | 100 |  | √ | ' ' | 操作项编码 |
| 27 | fperm_item_id | 权限项ID | varchar | 36 |  | √ | ' ' | 权限项ID |
| 28 | fclient_ip | 客户端地址 | varchar | 300 |  | √ | ' ' | 客户端地址 |
| 29 | fmodify_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 30 | fclient_name | 客户端名称 | varchar | 300 |  | √ | ' ' | 客户端名称 |
| 31 | fform_identity | 表单标识 | varchar | 50 |  | √ | ' ' | 表单标识 |
| 32 | fbusi_from | 业务来源 | varchar | 100 |  | √ | ' ' | 业务来源 |
| 33 | foper_time | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 34 | fnumber | 操作编码 | varchar | 50 |  | √ | ' ' | 操作编码 |
| 35 | fpre_data | 操作前数据 | text | 0 |  |  | null | 操作前数据 |
| 36 | fapp_id | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_archive |  | fid |
| 2 | idx_pl_arch_optime |  | foper_time |
