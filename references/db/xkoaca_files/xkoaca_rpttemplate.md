# 经营报表模板-xkoaca_rpttemplate

## 经营报表模板-多语言表 t_xkoaca_rpttpl_l

- **表名称：** 经营报表模板-多语言表
- **表名：** t_xkoaca_rpttpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 报表名称 | varchar | 255 |  | √ | ' ' | 报表名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rpttpl_l |  | fpkid |
| 2 | idx_xkoaca_rpttpl_l |  | fid,flocaleid |

---

## 列设置-多语言表 t_xkoaca_rpttplcolentry_l

- **表名称：** 列设置-多语言表
- **表名：** t_xkoaca_rpttplcolentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fcolnamelang | 列名称 | varchar | 255 |  | √ | ' ' | 列名称 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoaca_rpttplcolentry_l |  | fentryid,flocaleid |
| 2 | pk_xkoaca_rpttplcolentry_l |  | fpkid |

---

## 经营报表模板-主表 t_xkoaca_rpttpl

- **表名称：** 经营报表模板-主表
- **表名：** t_xkoaca_rpttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 3 | frowsrcdim | 行维度 | bpchar | 1 |  | √ | ' ' | 行维度,枚举: 1 :经营主体+时间维度 2 :经营指标+时间维度 3 :经营主体+经营指标 4 :经营主体 5 :时间维度 6 :经营指标 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcolsrcdim | 列维度 | bpchar | 1 |  | √ | ' ' | 列维度,枚举: 1 :经营主体+时间维度 2 :经营指标+时间维度 3 :经营主体+经营指标 4 :经营主体 5 :时间维度 6 :经营指标 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftpltype | 模板类型 | varchar | 2 |  | √ | ' ' | 模板类型,枚举: 1 :经营费用分析 2 :经营利润分析 3 :经营收入分析 4 :经营达成率 |
| 12 | fusecount | 使用次数 | int4 | 32 |  | √ | 0 | 使用次数 |
| 13 | fcolmaxkey | 最大列标识 | int4 | 32 |  | √ | 0 | 最大列标识 |
| 14 | frowmaxkey | 最大行标识 | int4 | 32 |  | √ | 0 | 最大行标识 |
| 15 | fname | 报表名称 | varchar | 255 |  | √ | ' ' | 报表名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fpublishstatus | 发布状态 | bpchar | 1 |  | √ | '0' | 发布状态 |
| 18 | fkeep | 是否收藏 | bpchar | 1 |  | √ | '0' | 是否收藏 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 21 | fdisableperson | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fsector | 所属行业 | varchar | 2 |  | √ | ' ' | 所属行业,枚举: 1 :通用 2 :餐饮 3 :食品 |
| 25 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rpttpl |  | fid |
| 2 | idx_xkoaca_rpttpl_fnum |  | fnumber |

---

## 列设置-子表 t_xkoaca_rpttplcolentry

- **表名称：** 列设置-子表
- **表名：** t_xkoaca_rpttplcolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcolhidden | 隐藏列 | bpchar | 1 |  | √ | '0' | 隐藏列 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcolrptdim | 维度来源 | int8 | 64 |  | √ | 0 | [经营报表维度 xkoaca_reportdimension](../xkoaca_files/xkoaca_reportdimension.md) |
| 5 | fcolformula_tag | 取数公式设置_详情 | text | 0 |  |  | null | 取数公式设置_详情 |
| 6 | fcolprop | 列属性 | bpchar | 1 |  | √ | '1' | 列属性,枚举: 1 :维度项 2 :计算项 3 :文本项 |
| 7 | fcolformuladesc | 取数公式 | varchar | 2000 |  | √ | ' ' | 取数公式 |
| 8 | fcolname | 列名称（废弃） | varchar | 100 |  | √ | ' ' | 列名称（废弃） |
| 9 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 10 | fcolformula | 取数公式设置 | text | 0 |  |  | null | 取数公式设置 |
| 11 | fcolnamelang | 列名称 | varchar | 255 |  | √ | ' ' | 列名称 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcolkey | 列标识 | varchar | 10 |  | √ | ' ' | 列标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rpttplcolentry |  | fentryid |
| 2 | idx_xkoaca_rpttolcolentry_fid |  | fid |

---

## 行设置-多语言表 t_xkoaca_rpttplrowentry_l

- **表名称：** 行设置-多语言表
- **表名：** t_xkoaca_rpttplrowentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | frownamelang | 行名称 | varchar | 255 |  | √ | ' ' | 行名称 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rpttplrowentry_l |  | fpkid |
| 2 | idx_xkoaca_rpttplrowentry_l |  | fentryid,flocaleid |

---

## 经营账簿-多选基础资料表 t_xkoaca_rpttpl_opbk

- **表名称：** 经营账簿-多选基础资料表
- **表名：** t_xkoaca_rpttpl_opbk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rpttpl_opbk |  | fpkid |
| 2 | idx_xkoaca_rpttpl_opbk |  | fid |

---

## 行设置-子表 t_xkoaca_rpttplrowentry

- **表名称：** 行设置-子表
- **表名：** t_xkoaca_rpttplrowentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowformula_tag | 取数公式设置_详情 | text | 0 |  |  | null | 取数公式设置_详情 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | frowrptdim | 维度来源 | int8 | 64 |  | √ | 0 | [经营报表维度 xkoaca_reportdimension](../xkoaca_files/xkoaca_reportdimension.md) |
| 5 | frownamelang | 行名称 | varchar | 255 |  | √ | ' ' | 行名称 |
| 6 | frowformuladesc | 取数公式 | varchar | 2000 |  | √ | ' ' | 取数公式 |
| 7 | frowhidden | 隐藏行 | bpchar | 1 |  | √ | '0' | 隐藏行 |
| 8 | frowname | 行名称（废弃） | varchar | 100 |  | √ | ' ' | 行名称（废弃） |
| 9 | frowformula | 取数公式设置 | text | 0 |  |  | null | 取数公式设置 |
| 10 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 11 | frowkey | 行标识 | varchar | 10 |  | √ | ' ' | 行标识 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | frowprop | 行属性 | bpchar | 1 |  | √ | '1' | 行属性,枚举: 1 :维度项 2 :计算项 3 :文本项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoaca_rpttolrowentry_fid |  | fid |
| 2 | pk_xkoaca_rpttplrowentry |  | fentryid |
