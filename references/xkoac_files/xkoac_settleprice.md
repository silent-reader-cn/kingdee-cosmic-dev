# 经营单元结算价目表-xkoac_settleprice

## 适用经营账簿-多选基础资料表 t_xkoac_setpricebook

- **表名称：** 适用经营账簿-多选基础资料表
- **表名：** t_xkoac_setpricebook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 经营账簿 xkoac_operatingbook |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_setpricebook |  | fbasedataid |
| 2 | pk_t_xkoac_setpricebook |  | fpkid |

---

## 单据体-子表 t_xkoac_setpriceentry

- **表名称：** 单据体-子表
- **表名：** t_xkoac_setpriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fupdatedtime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 7 | fpresetprice1 | 预留单价1 | numeric | 23 | 10 | √ | 0 | 预留单价1 |
| 8 | fpresetprice2 | 预留单价2 | numeric | 23 | 10 | √ | 0 | 预留单价2 |
| 9 | fpresetprice3 | 预留单价3 | numeric | 23 | 10 | √ | 0 | 预留单价3 |
| 10 | fpricegetmode | 来源类型 | bpchar | 1 |  |  | '1' | 来源类型,枚举: 1 :手工录入 |
| 11 | fexpiredate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 12 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | pricegetmode | pricegetmode | bpchar | 1 |  | √ | '1' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_setpriceentry |  | fid |
| 2 | pk_t_xkoac_setpriceentry |  | fentryid |

---

## 卖方经营单元-多选基础资料表 t_xkoac_setpriceseller

- **表名称：** 卖方经营单元-多选基础资料表
- **表名：** t_xkoac_setpriceseller

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 经营单元 xkoac_unit |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_setpriceseller |  | fbasedataid |
| 2 | pk_t_xkoac_setpriceseller |  | fpkid |

---

## 经营单元结算价目表-主表 t_xkoac_settleprice

- **表名称：** 经营单元结算价目表-主表
- **表名：** t_xkoac_settleprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fapprovedate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 4 | fpricetype | 定价类型 | bpchar | 1 |  | √ | '2' | 定价类型,枚举: 1 :单边定价 2 :双边定价 3 :通用定价 |
| 5 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fpriceobj | 价目表对象 | bpchar | 1 |  | √ | '1' | 价目表对象,枚举: 1 :物料 2 :物料分类 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 16 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_settleprice |  | fid |
| 2 | idx_xkoac_settleprice_fnum |  | fnumber |

---

## 经营单元结算价目表-多语言表 t_xkoac_settleprice_l

- **表名称：** 经营单元结算价目表-多语言表
- **表名：** t_xkoac_settleprice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_settleprice_l |  | fpkid |
| 2 | idx_xkoac_settprice_l |  | fid,flocaleid |

---

## 买方经营单元-多选基础资料表 t_xkoac_setpricebuyer

- **表名称：** 买方经营单元-多选基础资料表
- **表名：** t_xkoac_setpricebuyer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 经营单元 xkoac_unit |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_setpricebuyer |  | fbasedataid |
| 2 | pk_t_xkoac_setpricebuyer |  | fpkid |
