# 可发量单据配置-sm_expectqtybillsetting

## 可发量单据配置-多语言表 t_sm_expectqtybillsetting_l

- **表名称：** 可发量单据配置-多语言表
- **表名：** t_sm_expectqtybillsetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 128 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_expectqtybillsetting_l |  | fpkid |
| 2 | idx_sm_expectqtybillsetting_l |  | fid,flocaleid |

---

## 字段携带配置-子表 t_sm_expectqtyfieldcarry

- **表名称：** 字段携带配置-子表
- **表名：** t_sm_expectqtyfieldcarry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fenable | 携带 | bpchar | 1 |  | √ | '0' | 携带 |
| 4 | fcarryfield | 携带字段 | varchar | 50 |  | √ | ' ' | 携带字段 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_expectqtyfieldcarry |  | fid |
| 2 | pk_sm_expectqtyfieldcarry |  | fentryid |

---

## 可发量操作配置-多语言表 t_sm_expectqtyoperateset_l

- **表名称：** 可发量操作配置-多语言表
- **表名：** t_sm_expectqtyoperateset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foperationname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_expectqtyoperateset_l |  | fentryid,flocaleid |
| 2 | pk_sm_expectqtyoperateset_l |  | fpkid |

---

## 可发量操作配置-子表 t_sm_expectqtyoperateset

- **表名称：** 可发量操作配置-子表
- **表名：** t_sm_expectqtyoperateset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | foperationname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 4 | fenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 5 | foperation | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称,枚举: |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_expectqtyoperateset |  | fid |
| 2 | pk_sm_expectqtyoperateset |  | fentryid |

---

## 可发量单据配置-主表 t_sm_expectqtybillsetting

- **表名称：** 可发量单据配置-主表
- **表名：** t_sm_expectqtybillsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvdirection | 库存方向 | bpchar | 1 |  | √ | ' ' | 库存方向,枚举: 0 :普通 1 :退货 |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fbillentrykey | 单据明细 | varchar | 50 |  | √ | ' ' | 单据明细,枚举: |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  |  | 0 | 主数据内码 |
| 10 | fformula | fformula | varchar | 200 |  | √ | ' ' |  |
| 11 | ffilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 12 | fsupplysourcetype | 供应来源类别 | bpchar | 1 |  | √ | ' ' | 供应来源类别,枚举: 0 :客户 1 :供应商 2 :部门 |
| 13 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 14 | fformid | 单据名称 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  |  | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | 名称 | varchar | 128 |  | √ | ' ' | 名称 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 20 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | ' ' | 过滤条件_详情 |
| 21 | fexpectqtydirection | 预计可发量方向 | bpchar | 1 |  | √ | ' ' | 预计可发量方向,枚举: 0 :预计出 1 :预计入 |
| 22 | fonlyprocesscurrow | 仅处理光标所在当前行 | bpchar | 1 |  | √ | '0' | 仅处理光标所在当前行 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | ffilterdesc | 过滤条件描述 | varchar | 500 |  | √ | ' ' | 过滤条件描述 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_expectqtybillsetting |  | fid |
| 2 | idx_sm_expectqtybillsetting |  | fnumber |

---

## 计算单位匹配及其他-子表 t_sm_expectqtyfieldmap_s3

- **表名称：** 计算单位匹配及其他-子表
- **表名：** t_sm_expectqtyfieldmap_s3

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpectqtyfieldname | fexpectqtyfieldname | varchar | 50 |  | √ | ' ' |  |
| 3 | fexpectqtyfield | 可发量字段 | varchar | 50 |  | √ | ' ' | 可发量字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbillmapfieldname | fbillmapfieldname | varchar | 50 |  | √ | ' ' |  |
| 6 | fbillmapfield | 单据对应字段 | varchar | 50 |  | √ | ' ' | 单据对应字段 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_expectqtyfieldmap_s3 |  | fentryid |
| 2 | idx_sm_expectqtyfieldmap_s3 |  | fid |

---

## 单据上获取可发量字段对应-子表 t_sm_expectqtyfieldmap_s4

- **表名称：** 单据上获取可发量字段对应-子表
- **表名：** t_sm_expectqtyfieldmap_s4

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpectqtyfieldname | fexpectqtyfieldname | varchar | 50 |  | √ | ' ' |  |
| 3 | fexpectqtyfield | 可发量输出字段 | varchar | 50 |  | √ | ' ' | 可发量输出字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbillmapfieldname | fbillmapfieldname | varchar | 50 |  | √ | ' ' |  |
| 6 | fbillmapfield | 单据对应字段 | varchar | 50 |  | √ | ' ' | 单据对应字段 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_expectqtyfieldmap_s4 |  | fentryid |
| 2 | idx_sm_expectqtyfieldmap_s4 |  | fid |

---

## 预计出\预计入字段配置-子表 t_sm_expectqtyfieldmap_s1

- **表名称：** 预计出\预计入字段配置-子表
- **表名：** t_sm_expectqtyfieldmap_s1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpectqtyfieldname | fexpectqtyfieldname | varchar | 50 |  | √ | ' ' |  |
| 3 | fexpectqtyfield | 可发量计算字段 | varchar | 50 |  | √ | ' ' | 可发量计算字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbillmapfieldname | fbillmapfieldname | varchar | 50 |  | √ | ' ' |  |
| 6 | fbillmapfield | 单据对应字段 | varchar | 50 |  | √ | ' ' | 单据对应字段 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_expectqtyfieldmap_s1 |  | fentryid |
| 2 | idx_sm_expectqtyfieldmap_s1 |  | fid |

---

## 单据控制可发量匹配字段设置-子表 t_sm_expectqtyfieldmap_s2

- **表名称：** 单据控制可发量匹配字段设置-子表
- **表名：** t_sm_expectqtyfieldmap_s2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpectqtyfieldname | fexpectqtyfieldname | varchar | 50 |  | √ | ' ' |  |
| 3 | fexpectqtyfield | 可发量字段 | varchar | 50 |  | √ | ' ' | 可发量字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbillmapfieldname | fbillmapfieldname | varchar | 50 |  | √ | ' ' |  |
| 6 | fbillmapfield | 单据对应字段 | varchar | 50 |  | √ | ' ' | 单据对应字段 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_expectqtyfieldmap_s2 |  | fentryid |
| 2 | idx_sm_expectqtyfieldmap_s2 |  | fid |
