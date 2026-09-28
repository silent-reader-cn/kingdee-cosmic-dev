# 集成资源导入-isc_dts_imp

## 主资源-子表 t_iscb_dts_imp_mrs2

- **表名称：** 主资源-子表
- **表名：** t_iscb_dts_imp_mrs2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 资源名称 | varchar | 255 |  | √ | ' ' | 资源名称 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fres_pk | 资源ID | varchar | 50 |  | √ | ' ' | 资源ID |
| 5 | ffile | 资源文件 | varchar | 150 |  | √ | ' ' | 资源文件 |
| 6 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: READY :就绪 SUCCESS :成功 FAILED :失败 OMITTED :忽略 |
| 7 | flocal_time | 本地最近修改时间 | timestamp | 0 |  |  | null | 本地最近修改时间 |
| 8 | ftype | 资源类型 | varchar | 150 |  | √ | ' ' | 资源类型 |
| 9 | fstack_trace | fstack_trace | text | 0 |  |  | null |  |
| 10 | fsource_trace | 资源追溯 | varchar | 600 |  | √ | ' ' | 资源追溯 |
| 11 | fnumber | 资源编码 | varchar | 255 |  | √ | ' ' | 资源编码 |
| 12 | foperation | 导入方式 | varchar | 50 |  | √ | ' ' | 导入方式,枚举: INSERT :新增 UPDATE :覆盖 |
| 13 | fcontent | fcontent | text | 0 |  |  | null |  |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fres_time | 资源最近修改时间 | timestamp | 0 |  |  | null | 资源最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_t_iscb_dts_imp_mrs2 |  | fid |
| 2 | pk_t_iscb_dts_imp_mrs2 |  | fentryid |

---

## 集成资源导入-主表 t_iscb_dts_imp_header

- **表名称：** 集成资源导入-主表
- **表名：** t_iscb_dts_imp_header

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fres_version | fres_version | varchar | 50 |  | √ | ' ' |  |
| 7 | fres_id | fres_id | varchar | 50 |  | √ | ' ' |  |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fprogress | 进度 | varchar | 50 |  | √ | ' ' | 进度,枚举: READY :暂存 PARSING :解析中 PARSED :已解析 IMPORTED :已导入 IMPORTING :导入中 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fres_type | 资源类型 | varchar | 150 |  | √ | ' ' | 资源类型 |
| 12 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: READY :就绪 SUCCESS :已结束 FAILED :失败 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillno | 任务批号 | varchar | 30 |  | √ | ' ' | 任务批号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_t_iscb_dts_header |  | fbillno |
| 2 | pk_t_iscb_dts_imp_header |  | fid |

---

## 依赖资源-子表 t_iscb_dts_imp_rrs2

- **表名称：** 依赖资源-子表
- **表名：** t_iscb_dts_imp_rrs2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 资源名称 | varchar | 255 |  | √ | ' ' | 资源名称 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fres_pk | 资源ID | varchar | 50 |  | √ | ' ' | 资源ID |
| 5 | ffile | 资源文件 | varchar | 150 |  | √ | ' ' | 资源文件 |
| 6 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: READY :就绪 SUCCESS :成功 FAILED :失败 OMITTED :忽略 |
| 7 | flocal_time | 本地最近修改时间 | timestamp | 0 |  |  | null | 本地最近修改时间 |
| 8 | ftype | 资源类型 | varchar | 150 |  | √ | ' ' | 资源类型 |
| 9 | fstack_trace | fstack_trace | text | 0 |  |  | null |  |
| 10 | fsource_trace | 资源追溯 | varchar | 600 |  | √ | ' ' | 资源追溯 |
| 11 | fnumber | 资源编码 | varchar | 255 |  | √ | ' ' | 资源编码 |
| 12 | foperation | 导入方式 | varchar | 50 |  | √ | ' ' | 导入方式,枚举: INSERT :关联 UPDATE :覆盖 |
| 13 | fcontent | fcontent | text | 0 |  |  | null |  |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fres_time | 资源最近修改时间 | timestamp | 0 |  |  | null | 资源最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_dts_imp_rrs2 |  | fentryid |
| 2 | index_t_iscb_dts_imp_rrs2 |  | fid |
