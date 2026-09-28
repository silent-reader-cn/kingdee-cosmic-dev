# 下载中心-rim_download_center

## 下载中心-主表 t_rim_download_center

- **表名称：** 下载中心-主表
- **表名：** t_rim_download_center

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstate | 处理状态 | varchar | 4 |  | √ | ' ' | 处理状态,枚举: 1 :处理中 2 :处理完成 3 :处理失败 4 :已清理 |
| 3 | fservice_url | fservice_url | varchar | 400 |  | √ | ' ' |  |
| 4 | ffile_type | 文件类型 | varchar | 150 |  | √ | ' ' | 文件类型 |
| 5 | fapplytime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 6 | fapplicant | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fsource | 下载类型 | varchar | 4 |  | √ | ' ' | 下载类型,枚举: 0 :导出发票Excel 1 :发票文件下载 |
| 8 | fbillno | 文件名称 | varchar | 40 |  | √ | ' ' | 文件名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_download_center |  | fid |
| 2 | idx_rim_download_center |  | fbillno |

---

## 单据体-子表 t_rim_download_uplodetail

- **表名称：** 单据体-子表
- **表名：** t_rim_download_uplodetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fservice_url | 服务器文件地址 | varchar | 400 |  | √ | ' ' | 服务器文件地址 |
| 3 | ffilename | 文件名 | varchar | 250 |  | √ | ' ' | 文件名 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fresult | fresult | varchar | 10 |  | √ | ' ' |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_download_uplodetail |  | fentryid |
| 2 | idx_rim_download_fk |  | fid |

---

## 单据体-子表 t_rim_download_detail

- **表名称：** 单据体-子表
- **表名：** t_rim_download_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | furl_type | 处理结果 | varchar | 4 |  | √ | ' ' | 处理结果,枚举: 0 :处理中 1 :处理成功 2 :处理失败 3 :处理成功（空） 4 :处理成功（重复） |
| 3 | fserial_no | 发票号码+代码 | varchar | 40 |  | √ | ' ' | 发票号码+代码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | finvoice_url | 文件URL | varchar | 200 |  | √ | ' ' | 文件URL |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_download_detail |  | fid |
| 2 | pk_rim_download_detail |  | fentryid |
