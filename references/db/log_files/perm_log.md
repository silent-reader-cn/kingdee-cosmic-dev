# 权限日志-perm_log

## 权限日志-主表 t_perm_log

- **表名称：** 权限日志-主表
- **表名：** t_perm_log

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
| 8 | ffrom_backup | 是否归档还原而来 | bpchar | 1 |  | √ | '0' | 是否归档还原而来 |
| 9 | fperm_item_name | 权限项名 | varchar | 50 |  | √ | ' ' | 权限项名 |
| 10 | ffiling_time | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 11 | fdiff_content | 差异内容 | text | 0 |  |  | null | 差异内容 |
| 12 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 13 | fafter_data | 操作后数据 | text | 0 |  |  | null | 操作后数据 |
| 14 | fop_item_id | 操作项ID | varchar | 100 |  | √ | ' ' | 操作项ID |
| 15 | foper_number | 操作用户工号 | varchar | 36 |  | √ | ' ' | 操作用户工号 |
| 16 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fop_item_name | 操作项名称 | varchar | 100 |  | √ | ' ' | 操作项名称 |
| 18 | fop_desc | 操作描述 | text | 0 |  |  | null | 操作描述 |
| 19 | fform_name | 表单名称 | varchar | 200 |  | √ | ' ' | 表单名称 |
| 20 | foper_username | 操作用户用户名 | varchar | 255 |  | √ | ' ' | 操作用户用户名 |
| 21 | foper_org_name | 操作组织名 | varchar | 50 |  | √ | ' ' | 操作组织名 |
| 22 | fclient_type | 客户端类型 | varchar | 300 |  | √ | ' ' | 客户端类型,枚举: web :PC端 mobile :移动端 api :接口 |
| 23 | fcloud_name | 云名称 | varchar | 100 |  | √ | ' ' | 云名称 |
| 24 | foper_id | 操作用户ID | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | foper_org_id | 操作组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fopbtn | 操作按钮名称 | varchar | 100 |  | √ | ' ' | 操作按钮名称 |
| 27 | fop_item_number | 操作项编码 | varchar | 100 |  | √ | ' ' | 操作项编码 |
| 28 | fperm_item_id | 权限项ID | varchar | 36 |  | √ | ' ' | 权限项ID |
| 29 | fclient_ip | 客户端地址 | varchar | 300 |  | √ | ' ' | 客户端地址 |
| 30 | fmodify_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 31 | fclient_name | 客户端名称 | varchar | 300 |  | √ | ' ' | 客户端名称 |
| 32 | fgendiff_result | 生成差异结果信息 | varchar | 300 |  | √ | ' ' | 生成差异结果信息 |
| 33 | fform_identity | 表单标识 | varchar | 50 |  | √ | ' ' | 表单标识 |
| 34 | fbusi_from | 业务来源 | varchar | 100 |  | √ | ' ' | 业务来源 |
| 35 | foper_time | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 36 | fnumber | 操作编码 | varchar | 50 |  | √ | ' ' | 操作编码 |
| 37 | fpre_data | 操作前数据 | text | 0 |  |  | null | 操作前数据 |
| 38 | fapp_id | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid,fnumber |
| 2 | fnumber | fid,fnumber |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_foper_time |  | foper_time |
| 2 | pk_perm_log |  | fid,fnumber |
