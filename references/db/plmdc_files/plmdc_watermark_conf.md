# 水印内容配置-plmdc_watermark_conf

## 水印内容信息配置-子表 t_plmdc_watermkcof_entry

- **表名称：** 水印内容信息配置-子表
- **表名：** t_plmdc_watermkcof_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattusingmode | 使用模式 | varchar | 50 |  | √ | ' ' | 使用模式,枚举: A :完全取值 B :分区间段编码 C :整段编码 |
| 3 | flabelapnum | 编码段 | varchar | 50 |  | √ | ' ' | 编码段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffixval | 设置值 | varchar | 50 |  | √ | ' ' | 设置值 |
| 6 | fsplitsignentry | 段间分隔符 | varchar | 50 |  | √ | ' ' | 段间分隔符,枚举: * :* - :- empty :空 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fattributetype | 属性类型 | varchar | 50 |  | √ | ' ' | 属性类型,枚举: 1 :常量 8 :业务对象字段 |
| 9 | fvalueatributeshow | 编码来源 | varchar | 50 |  | √ | ' ' | 编码来源 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_watermkcof_entry |  | fentryid |
| 2 | idx_plmdc_watermkcof_entry_fid |  | fid |

---

## 水印内容配置-主表 t_plmdc_watermark_conf

- **表名称：** 水印内容配置-主表
- **表名：** t_plmdc_watermark_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fexample | 文本示例 | varchar | 500 |  | √ | ' ' | 文本示例 |
| 4 | fnumber | 编码 | varchar | 500 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_watermark_conf |  | fid |
| 2 | idx_plmdc_wm_conf_fnumber |  | fnumber |
