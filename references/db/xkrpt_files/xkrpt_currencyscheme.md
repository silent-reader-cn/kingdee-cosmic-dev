# 折算方案-xkrpt_currencyscheme

## 合并范围-多选基础资料表 t_xkrpt_currscheme_scope

- **表名称：** 合并范围-多选基础资料表
- **表名：** t_xkrpt_currscheme_scope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 合并范围 xkcr_scope |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_currscheme_scope |  | fid |
| 2 | pk_t_xkrpt_currscheme_scope |  | fpkid |

---

## 折算方案-主表 t_xkrpt_currencyscheme

- **表名称：** 折算方案-主表
- **表名：** t_xkrpt_currencyscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemschemeid | 报表项目关联折算方法 | int8 | 64 |  | √ | 0 | 报表项目关联折算方法 xkrpt_projectcurrencytran |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | frateprecision | 汇率精度 | int4 | 32 |  | √ | 4 | 汇率精度 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fscopetype | 合并方案 | int8 | 64 |  | √ | 0 | 合并方案 xkcr_scopetype |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fratetypeid | 汇率类型 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 17 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 18 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | ftarcurrencyid | 折算目标币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fscope | 合并范围 | int8 | 64 |  | √ | 0 | 合并范围 xkcr_scope |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_currencyscheme |  | fnumber |
| 2 | pk_t_xkrpt_currencyscheme |  | fid |

---

## 币别-多选基础资料表 t_xkrpt_currscheme_curr

- **表名称：** 币别-多选基础资料表
- **表名：** t_xkrpt_currscheme_curr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_currscheme_curr |  | fid |
| 2 | pk_t_xkrpt_currscheme_curr |  | fpkid |

---

## 报表模板-多选基础资料表 t_xkrpt_currscheme_temp

- **表名称：** 报表模板-多选基础资料表
- **表名：** t_xkrpt_currscheme_temp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 报表模板 xkrpt_rptsample |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_currscheme_temp |  | fpkid |
| 2 | idx_xkrpt_currscheme_temp |  | fid |

---

## 报表项目-多选基础资料表 t_xkrpt_currscheme_item

- **表名称：** 报表项目-多选基础资料表
- **表名：** t_xkrpt_currscheme_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_currscheme_item |  | fid |
| 2 | pk_t_xkrpt_currscheme_item |  | fpkid |

---

## 组织-多选基础资料表 t_xkrpt_currscheme_org

- **表名称：** 组织-多选基础资料表
- **表名：** t_xkrpt_currscheme_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_currscheme_org |  | fpkid |
| 2 | idx_xkrpt_currscheme_org |  | fid |

---

## 折算方案-多语言表 t_xkrpt_currencyscheme_l

- **表名称：** 折算方案-多语言表
- **表名：** t_xkrpt_currencyscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_currencyscheme_l |  | fpkid |
| 2 | idx_xkrpt_currencyscheme_l |  | fid,flocaleid |

---

## 差异项目公式设置单据体-子表 t_xkrpt_cts_diffdataitem

- **表名称：** 差异项目公式设置单据体-子表
- **表名：** t_xkrpt_cts_diffdataitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiffitemformula | 差异项目公式 | varchar | 255 |  | √ | ' ' | 差异项目公式 |
| 3 | fdiffitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdiffitemid | 折算差异项目 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_cts_diffdataitem_fid |  | fid |
| 2 | pk_t_xkrpt_cts_diffdataitem |  | fentryid |

---

## 项目数据类型-多选基础资料表 t_xkrpt_currscheme_type

- **表名称：** 项目数据类型-多选基础资料表
- **表名：** t_xkrpt_currscheme_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_currscheme_type |  | fid |
| 2 | pk_t_xkrpt_currscheme_type |  | fpkid |
