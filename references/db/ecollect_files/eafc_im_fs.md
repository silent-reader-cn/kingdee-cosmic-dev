# 文件服务器-eafc_im_fs

## 文件服务器-多语言表 tk_eafc_im_fs_l

- **表名称：** 文件服务器-多语言表
- **表名：** tk_eafc_im_fs_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_fs_l |  | fpkid |

---

## 文件服务器-主表 tk_eafc_im_fs

- **表名称：** 文件服务器-主表
- **表名：** tk_eafc_im_fs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_fs_user | 登录用户 | varchar | 50 |  | √ | ' ' | 登录用户 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 50 |  |  | null |  |
| 5 | fk_eafc_fs_pwd | 登录密码 | varchar | 50 |  | √ | ' ' | 登录密码 |
| 6 | fk_eafc_nfs_path | 挂载点 | varchar | 50 |  | √ | ' ' | 挂载点 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fk_eafc_fs_ip | 服务器IP或域名 | varchar | 50 |  | √ | ' ' | 服务器IP或域名 |
| 9 | fk_eafc_fs_port | 服务器端口 | int8 | 64 |  |  | null | 服务器端口 |
| 10 | fk_eafc_work_dir | 工作目录 | varchar | 501 |  | √ | ' ' | 工作目录 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 15 | fk_eafc_combofield | 文件服务器类型 | varchar | 50 |  | √ | ' ' | 文件服务器类型,枚举: 1 :FTP 2 :Minio 3 :星瀚财务云（多租户） 4 :NFS 5 :SFTP |
| 16 | fk_eafc_fs_bucket | 存储桶 | varchar | 50 |  | √ | ' ' | 存储桶 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_fs |  | fid |

---

## 单据体-子表 tk_eafc_im_fs_item

- **表名称：** 单据体-子表
- **表名：** tk_eafc_im_fs_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_accountid | 数据中心ID | varchar | 50 |  | √ | ' ' | 数据中心ID |
| 3 | fk_eafc_erpurl | 苍穹地址 | varchar | 100 |  | √ | ' ' | 苍穹地址 |
| 4 | fk_eafc_appid | 第三方appId | varchar | 50 |  | √ | ' ' | 第三方appId |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_user | 用户 | varchar | 50 |  | √ | ' ' | 用户 |
| 7 | fk_eafc_tenantid | 租户ID | varchar | 50 |  | √ | ' ' | 租户ID |
| 8 | fk_eafc_usertype | 用户标识 | varchar | 50 |  | √ | ' ' | 用户标识,枚举: Mobile :手机号 Email :邮箱 UserName :用户名 |
| 9 | fk_eafc_appsecret | 第三方app密码 | varchar | 50 |  | √ | ' ' | 第三方app密码 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_fs_item |  | fentryid |
