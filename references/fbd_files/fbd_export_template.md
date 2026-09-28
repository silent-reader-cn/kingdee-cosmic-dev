# 网银引出模版-fbd_export_template

## 报文体设置分录-子表 t_fbd_ebankexportentry

- **表名称：** 报文体设置分录-子表
- **表名：** t_fbd_ebankexportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgetvaluetype | 取值类型 | varchar | 50 |  | √ | ' ' | 取值类型,枚举: 01 :源单字段 02 :固定值 |
| 3 | fgetvaluedesc | 取值 | varchar | 1000 |  | √ | ' ' | 取值 |
| 4 | flength | 长度 | int2 | 16 |  | √ | 0 | 长度 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fgetvalue_tag | 取值条件_详情 | text | 0 |  |  | null | 取值条件_详情 |
| 7 | ffieldinstructions | 字段说明 | varchar | 255 |  | √ | ' ' | 字段说明 |
| 8 | fgetvalue | 取值条件 | varchar | 255 |  | √ | ' ' | 取值条件 |
| 9 | fmessagefield | 报文字段 | varchar | 50 |  | √ | ' ' | 报文字段 |
| 10 | fwillrecord | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 11 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: text :文本 money :金额 date :日期 serialnum :序号 |
| 12 | fmessagedesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_ebankexportentry |  | fentryid |
| 2 | idx_ebankexportentry_fid |  | fid |

---

## 网银引出模版-主表 t_fbd_ebankexport

- **表名称：** 网银引出模版-主表
- **表名：** t_fbd_ebankexport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fdatafilter | 数据过滤条件 | varchar | 255 |  | √ | ' ' | 数据过滤条件 |
| 5 | fcharset | 文件字符集 | varchar | 30 |  | √ | ' ' | 文件字符集,枚举: UTF-8 :UTF-8 ISO-8859-1 :ISO-8859-1 GBK :GBK GB2312 :GB2312 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbizobject | 业务对象 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fexportformatter | 引出格式 | varchar | 50 |  | √ | ' ' | 引出格式,枚举: 1 :xls 2 :txt |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fdatafilter_tag | 数据过滤条件_详情 | text | 0 |  |  | null | 数据过滤条件_详情 |
| 11 | ffootermessagedesc | ffootermessagedesc | varchar | 255 |  | √ | ' ' |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fisexport | 报文字段是否引出 | bpchar | 1 |  | √ | '1' | 报文字段是否引出 |
| 15 | fconditiondesc | 适用条件 | varchar | 1000 |  | √ | ' ' | 适用条件 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fmessagedesc | fmessagedesc | varchar | 255 |  | √ | ' ' |  |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 21 | fheadermessagedesc | fheadermessagedesc | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ebankexport_fnumber |  | fnumber |
| 2 | pk_t_fbd_ebankexport |  | fid |

---

## 报文尾设置分录-多语言表 t_fbd_ebankexpentry_f_l

- **表名称：** 报文尾设置分录-多语言表
- **表名：** t_fbd_ebankexpentry_f_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | ffootermessagedesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_ebankexpentry_f_l |  | fpkid |
| 2 | inx_ebankexpentry_f_l_feid |  | fentryid |

---

## 报文体设置分录-多语言表 t_fbd_ebankexportentry_l

- **表名称：** 报文体设置分录-多语言表
- **表名：** t_fbd_ebankexportentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmessagedesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_ebankexportentry_l |  | fpkid |
| 2 | idx_ebankexportentry_l_feid |  | fentryid |

---

## 网银引出模版-多语言表 t_fbd_ebankexport_l

- **表名称：** 网银引出模版-多语言表
- **表名：** t_fbd_ebankexport_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_ebankexport_l |  | fpkid |
| 2 | idx_ebankexport_l_fid |  | fid |

---

## 报文尾设置分录-子表 t_fbd_ebankexpentry_f

- **表名称：** 报文尾设置分录-子表
- **表名：** t_fbd_ebankexpentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffootergetvaluedesc | 取值 | varchar | 1000 |  | √ | ' ' | 取值 |
| 3 | ffootergetvaluetype | 取值类型 | varchar | 50 |  | √ | ' ' | 取值类型,枚举: 01 :源单字段 02 :固定值 |
| 4 | ffooterwillrecord | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | ffooterlength | 长度 | int2 | 16 |  | √ | 0 | 长度 |
| 7 | ffootermessagedesc | ffootermessagedesc | varchar | 255 |  | √ | ' ' |  |
| 8 | ffootermessagefield | 报文字段 | varchar | 50 |  | √ | ' ' | 报文字段 |
| 9 | ffooterfieldinstructions | 字段说明 | varchar | 255 |  | √ | ' ' | 字段说明 |
| 10 | ffooterfieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: text :文本 money :金额 date :日期 count :计数 |
| 11 | ffootergetvalue_tag | 取值条件_详情 | text | 0 |  |  | null | 取值条件_详情 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffootergetvalue | 取值条件 | varchar | 255 |  | √ | ' ' | 取值条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ebankexpentry_f_fid |  | fid |
| 2 | pk_t_fbd_ebankexpentry_f |  | fentryid |

---

## 报文头设置分录-子表 t_fbd_ebankexpentry_h

- **表名称：** 报文头设置分录-子表
- **表名：** t_fbd_ebankexpentry_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fheadergetvaluedesc | 取值 | varchar | 1000 |  | √ | ' ' | 取值 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fheaderlength | 长度 | int2 | 16 |  | √ | 0 | 长度 |
| 5 | fheadergetvaluetype | 取值类型 | varchar | 50 |  | √ | ' ' | 取值类型,枚举: 01 :源单字段 02 :固定值 |
| 6 | fheadermessagefield | 报文字段 | varchar | 50 |  | √ | ' ' | 报文字段 |
| 7 | fheaderfieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: text :文本 money :金额 date :日期 count :计数 |
| 8 | fheadergetvalue | 取值条件 | varchar | 255 |  | √ | ' ' | 取值条件 |
| 9 | fheaderwillrecord | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 10 | fheadergetvalue_tag | 取值条件_详情 | text | 0 |  |  | null | 取值条件_详情 |
| 11 | fheaderfieldinstructions | 字段说明 | varchar | 255 |  | √ | ' ' | 字段说明 |
| 12 | fheadermessagedesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_ebankexpentry_h |  | fentryid |
| 2 | idx_ebankexpentry_h_fid |  | fid |

---

## 报文头设置分录-多语言表 t_fbd_ebankexpentry_h_l

- **表名称：** 报文头设置分录-多语言表
- **表名：** t_fbd_ebankexpentry_h_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fheadermessagedesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_ebankexpentry_h_l |  | fpkid |
| 2 | idx_ebankexpentry_h_l_feid |  | fentryid |
