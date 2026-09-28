# 集成内容-eafc_im_content

## 集成内容-主表 tk_eafc_im_content

- **表名称：** 集成内容-主表
- **表名：** tk_eafc_im_content

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_file_archivetype | 主文件归档方式 | varchar | 50 |  | √ | ' ' | 主文件归档方式,枚举: 1 :下载接口或下载地址 2 :套打 3 :文件服务器 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 集成系统 | int8 | 64 |  |  | null | [集成系统 eafc_im_system](../ecollect_files/eafc_im_system.md) |
| 5 | fname | fname | varchar | 50 |  |  | null |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fk_eafc_printtpl | 旧套打模板 | varchar | 36 |  | √ | ' ' | [打印模板 bos_printtemplate](../mdl_files/bos_printtemplate.md) |
| 8 | fk_fpy_push_status | 启用状态回传 | bpchar | 1 |  | √ | '0' | 启用状态回传 |
| 9 | fk_eafc_fs | 主文件文件服务器 | int8 | 64 |  |  | null | [文件服务器 eafc_im_fs](../ecollect_files/eafc_im_fs.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fk_eafc_printtpl_new | 套打模板 | int8 | 64 |  | √ | 0 | [维护打印模板 bos_manageprinttpl](../cts_files/bos_manageprinttpl.md) |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fk_eafc_appen_archivetype | 附件归档方式 | varchar | 50 |  | √ | ' ' | 附件归档方式,枚举: 1 :下载接口或下载地址 3 :文件服务器 |
| 14 | fk_eafc_append_fs | 附件文件服务器 | int8 | 64 |  | √ | 0 | [文件服务器 eafc_im_fs](../ecollect_files/eafc_im_fs.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 内容编码 | varchar | 30 |  | √ | ' ' | 内容编码 |
| 19 | fk_eafc_desc | 内容描述 | varchar | 504 |  | √ | ' ' | 内容描述 |
| 20 | fk_eafc_business_type | 内容类型 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 21 | fk_fpy_encryption | 加密 | bpchar | 1 |  | √ | '0' | 加密 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_content |  | fid |

---

## 集成内容-多语言表 tk_eafc_im_content_l

- **表名称：** 集成内容-多语言表
- **表名：** tk_eafc_im_content_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 内容名称 | varchar | 50 |  | √ | ' ' | 内容名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_im_content_l |  | fpkid |

---

## 单据体-子表 tk_eafc_im_content_out

- **表名称：** 单据体-子表
- **表名：** tk_eafc_im_content_out

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_param_desc | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |
| 3 | fk_eafc_param_need | 是否必填 | bpchar | 1 |  | √ | '0' | 是否必填 |
| 4 | fk_eafc_param_name | 标准字段名 | varchar | 50 |  | √ | ' ' | 标准字段名 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_param_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: 1 :字符串 2 :整数 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 8 | fk_eafc_ds_param_name | 数据源字段名 | varchar | 50 |  | √ | ' ' | 数据源字段名 |
| 9 | fk_eafc_param_sysset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_im_content_out_fk |  | fid |
| 2 | pk__eafc_im_content_out |  | fentryid |
