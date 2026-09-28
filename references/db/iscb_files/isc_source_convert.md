# 数据源切换-isc_source_convert

## 资源列表-子表 t_iscb_dts_conv_rrs2

- **表名称：** 资源列表-子表
- **表名：** t_iscb_dts_conv_rrs2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fname | 资源名称 | varchar | 100 |  |  | null | 资源名称 |
| 3 | fnew_content | fnew_content | text | 0 |  |  | null |  |
| 4 | fseq | 分录行号 | int4 | 32 |  |  | null | 分录行号 |
| 5 | fres_pk | 资源ID | varchar | 50 |  |  | null | 资源ID |
| 6 | fnew_name | 资源名称（新） | varchar | 100 |  |  | null | 资源名称（新） |
| 7 | fnew_res_pk | 资源ID（新） | varchar | 50 |  |  | null | 资源ID（新） |
| 8 | fnew_number | 资源编码（新） | varchar | 100 |  |  | null | 资源编码（新） |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 10 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fstate | 状态 | varchar | 50 |  |  | null | 状态,枚举: READY :就绪 SUCCESS :成功 FAILED :失败 OMITTED :忽略 |
| 12 | ftype | 类型 | varchar | 36 |  |  | null | 业务对象 bos_objecttype |
| 13 | fstack_trace | fstack_trace | text | 0 |  |  | null |  |
| 14 | fnumber | 资源编码 | varchar | 100 |  |  | null | 资源编码 |
| 15 | fcontent | fcontent | text | 0 |  |  | null |  |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fres_time | 资源最近修改时间 | timestamp | 0 |  |  | null | 资源最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_dts_conv_rrs2_fk |  | fid |
| 2 | pk_t_iscb_dts_conv_rrs2 |  | fentryid |

---

## 单据体-子表 t_iscb_dts_ds_mapping

- **表名称：** 单据体-子表
- **表名：** t_iscb_dts_ds_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrc_pk | 源数据源ID | varchar | 50 |  |  | null | 源数据源ID |
| 3 | ftar_pk | 目标数据源ID | varchar | 50 |  |  | null | 目标数据源ID |
| 4 | fsrc_name | 源数据源名称 | varchar | 50 |  |  | null | 源数据源名称 |
| 5 | ftar_name | 目标数据源名称 | varchar | 50 |  |  | null | 目标数据源名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  |  | null | 分录行号 |
| 7 | fsrc_number | 源数据源编码 | varchar | 50 |  |  | null | 源数据源编码 |
| 8 | ftar_number | 目标数据源编码 | varchar | 50 |  |  | null | 目标数据源编码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_dts_ds_mapping_fk |  | fid |
| 2 | pk_t_iscb_dts_ds_mapping |  | fentryid |

---

## 数据源切换-主表 t_iscb_dts_src_convert

- **表名称：** 数据源切换-主表
- **表名：** t_iscb_dts_src_convert

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 150 |  |  | null | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsource_tenant | 来源 | varchar | 100 |  |  | null | 来源 |
| 7 | fauto_suffix | 编码自动加后缀 | bpchar | 1 |  | √ | '0' | 编码自动加后缀 |
| 8 | fisv | 资源开发商 | varchar | 100 |  |  | null | 资源开发商 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fprogress | 进度 | varchar | 50 |  |  | null | 进度,枚举: READY :暂存 PARSING :解析中 PARSED :已解析 CONVERTED :转换完成 CONVERTING :转换中 |
| 11 | fprotect_level | 资源保护等级 | varchar | 50 |  |  | null | 资源保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fres_type | 资源类型 | varchar | 36 |  |  | null | 业务对象 bos_objecttype |
| 14 | fstate | 状态 | varchar | 50 |  |  | null | 状态,枚举: READY :就绪 SUCCESS :已结束 FAILED :失败 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 16 | fsource_trace | 来源追溯 | varchar | 600 |  |  | null | 来源追溯 |
| 17 | fmode | 转换模式 | varchar | 50 |  |  | null | 转换模式,枚举: cover :覆盖 copy :复制 reset_trace :重置追溯信息 |
| 18 | fbillno | 单据编号 | varchar | 30 |  |  | null | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_dts_src_convert |  | fid |
| 2 | idx_iscb_src_conv_id |  | fbillno |
