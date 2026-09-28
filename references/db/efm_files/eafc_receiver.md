# 接收方配置-eafc_receiver

## 接收方配置-主表 tk_eafc_receiver

- **表名称：** 接收方配置-主表
- **表名：** tk_eafc_receiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_org | fk_eafc_org | int8 | 64 |  |  | null |  |
| 3 | fk_eafc_split_flag | 分条目封装 | bpchar | 1 |  | √ | '0' | 分条目封装 |
| 4 | fk_eafc_receive_mode | fk_eafc_receive_mode | varchar | 50 |  | √ | ' ' |  |
| 5 | fk_eafc_modifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fk_eafc_server_name | 文件服务器名称 | varchar | 100 |  | √ | ' ' | 文件服务器名称 |
| 7 | fk_eafc_notice_url | 请求地址 | varchar | 200 |  | √ | ' ' | 请求地址 |
| 8 | fk_eafc_receive_no | 接收方代码 | varchar | 50 |  | √ | ' ' | 接收方代码 |
| 9 | fk_eafc_createdate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fk_eafc_notice_flag | 启用归档通知 | bpchar | 1 |  | √ | '0' | 启用归档通知 |
| 11 | fk_eafc_deliver_api | 移交信息包接口（分片移交） | varchar | 300 |  | √ | ' ' | 移交信息包接口（分片移交） |
| 12 | fk_eafc_merge_api | 合并压缩包接口 | varchar | 300 |  | √ | ' ' | 合并压缩包接口 |
| 13 | fk_eafc_transfer_type | 传输方式 | varchar | 50 |  | √ | ' ' | 传输方式,枚举: 1 :API 2 :文件服务器 3 :自定义 |
| 14 | fk_eafc_recipient_mobile | fk_eafc_recipient_mobile | varchar | 30 |  | √ | ' ' |  |
| 15 | fk_eafc_account | 账户 | varchar | 100 |  | √ | ' ' | 账户 |
| 16 | fk_eafc_modifier | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fk_eafc_arcorg | fk_eafc_arcorg | int8 | 64 |  |  | null |  |
| 18 | fk_eafc_auth_api | 接收方授权接口 | varchar | 300 |  | √ | ' ' | 接收方授权接口 |
| 19 | fk_eafc_secret_key | 秘钥 | varchar | 100 |  | √ | ' ' | 秘钥 |
| 20 | fk_eafc_request_method | 请求方式 | varchar | 50 |  | √ | ' ' | 请求方式,枚举: 1 :POST 2 :GET |
| 21 | fk_eafc_creater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fk_eafc_server_type | 文件服务器类型 | varchar | 50 |  | √ | ' ' | 文件服务器类型,枚举: 1 :FTPS 2 :FTP 3 :MINIO 4 :SFTP |
| 23 | fk_eafc_server_address | 文件服务器地址 | varchar | 300 |  | √ | ' ' | 文件服务器地址 |
| 24 | fk_eafc_port | 端口 | varchar | 50 |  | √ | ' ' | 端口 |
| 25 | fk_eafc_ext_dept | fk_eafc_ext_dept | varchar | 100 |  | √ | ' ' |  |
| 26 | fk_eafc_split_num | 封装条目数 | int4 | 32 |  | √ | 0 | 封装条目数 |
| 27 | fk_eafc_reception_plan | 接收方案 | varchar | 50 |  | √ | ' ' | 接收方案,枚举: 1 :紫光 2 :量子伟业 |
| 28 | fk_eafc_dir_path | 服务器接收文件路径 | varchar | 100 |  | √ | ' ' | 服务器接收文件路径 |
| 29 | fk_eafc_ext_org | fk_eafc_ext_org | varchar | 100 |  | √ | ' ' |  |
| 30 | fk_eafc_app_id | 账户 | varchar | 100 |  | √ | ' ' | 账户 |
| 31 | fk_eafc_customize_class | 自定义实现类 | varchar | 300 |  | √ | ' ' | 自定义实现类 |
| 32 | fk_eafc_receive_type | fk_eafc_receive_type | varchar | 50 |  | √ | ' ' |  |
| 33 | fk_eafc_ext_recipient | fk_eafc_ext_recipient | varchar | 50 |  | √ | ' ' |  |
| 34 | fk_eafc_recipient | fk_eafc_recipient | int8 | 64 |  |  | null |  |
| 35 | fk_eafc_receive_name | 接收方系统名称 | varchar | 50 |  | √ | ' ' | 接收方系统名称 |
| 36 | fk_eafc_app_token | 秘钥 | varchar | 200 |  | √ | ' ' | 秘钥 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_receiver |  | fid |
