# 发票数据下载-bdm_download_center_v1

## 发票信息-子表 t_bdm_download_detail1

- **表名称：** 发票信息-子表
- **表名：** t_bdm_download_detail1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fserial_no | 发票号码+代码 | varchar | 50 |  | √ | ' ' | 发票号码+代码 |
| 3 | fdeal_result | 处理结果 | varchar | 50 |  | √ | ' ' | 处理结果,枚举: 0 :处理中 1 :处理成功 2 :处理失败 3 :处理成功（空） 4 :处理成功（重复） |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_download_detail1 |  | fentryid |
| 2 | idx_bdm_download_detail1_fk |  | fid |

---

## 文件信息-子表 t_bdm_download_detail2

- **表名称：** 文件信息-子表
- **表名：** t_bdm_download_detail2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetail_file_name | 文件名 | varchar | 50 |  | √ | ' ' | 文件名 |
| 3 | fdetail_url | 服务器文件地址 | varchar | 300 |  | √ | ' ' | 服务器文件地址 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_download_detail2 |  | fentryid |
| 2 | idx_bdm_download_detail2_fk |  | fid |

---

## 发票数据下载-主表 t_bdm_download_center

- **表名称：** 发票数据下载-主表
- **表名：** t_bdm_download_center

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqfilter | fqfilter | varchar | 255 |  | √ | ' ' |  |
| 3 | fhandlestate | 处理状态 | varchar | 30 |  | √ | ' ' | 处理状态,枚举: 1 :生成中 2 :处理完成 3 :处理失败 |
| 4 | fdelstate | 删除状态 | varchar | 30 |  | √ | ' ' | 删除状态,枚举: 1 :正常 2 :已删除 |
| 5 | fapplytime | 申请时间 | timestamp | 0 |  |  | null | 申请时间 |
| 6 | fapplicant | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ffileurl | 文件地址 | varchar | 200 |  | √ | ' ' | 文件地址 |
| 8 | fsource | 功能页面 | varchar | 50 |  | √ | ' ' | 功能页面 |
| 9 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fstarttime | 开票日期始 | timestamp | 0 |  |  | null | 开票日期始 |
| 11 | fappid | 数据来源 | varchar | 40 |  | √ | ' ' | 数据来源,枚举: sim :开票管理 rim :收票管理 |
| 12 | fqfilter_tag | fqfilter_tag | text | 0 |  |  | null |  |
| 13 | ffilename | 文件名称 | varchar | 100 |  | √ | ' ' | 文件名称 |
| 14 | ffile_type | 下载类型 | varchar | 8 |  | √ | ' ' | 下载类型,枚举: 1 :导出发票excel 2 :发票文件下载 |
| 15 | fnumber | 数量 | int8 | 64 |  | √ | 0 | 数量 |
| 16 | fendtime | 开票日期止 | timestamp | 0 |  |  | null | 开票日期止 |
| 17 | fexp_param | 请求参数 | varchar | 200 |  | √ | ' ' | 请求参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_download_center |  | fid |
| 2 | idx_bdm_download_center_id |  | fapplicant |
