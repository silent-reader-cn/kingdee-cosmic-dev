# 持股比例-xkcr_investrate

## 持股比例-主表 t_xkcr_investrate

- **表名称：** 持股比例-主表
- **表名：** t_xkcr_investrate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompanyfromid | 投资方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 5 | fperiod | 期 | int4 | 32 |  | √ | 0 | 期 |
| 6 | fcycle | 周期类型 | bpchar | 1 |  | √ | ' ' | 周期类型,枚举: |
| 7 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 8 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 9 | fbillno | 单据编号 | bpchar | 1 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_investrate_fcmp |  | fcompanyfromid |
| 2 | pk_xkcr_investrate |  | fid |

---

## 单据体-子表 t_xkcr_investrateentry

- **表名称：** 单据体-子表
- **表名：** t_xkcr_investrateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | felimtmpname | 对应抵销分录模板 | varchar | 2000 |  |  | ' ' | 对应抵销分录模板 |
| 3 | fcompanytoid | 被投资方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | frate | 持股比例 | numeric | 23 | 10 | √ | 0 | 持股比例 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcmpfromid | 投资方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fadjtmpname | 对应调整分录模板 | varchar | 2000 |  |  | ' ' | 对应调整分录模板 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_investrateentry_fin |  | fid |
| 2 | pk_xkcr_investrateentry |  | fentryid |

---

## 对应抵销分录模板-多选基础资料表 t_xkcr_investrateelimtmp

- **表名称：** 对应抵销分录模板-多选基础资料表
- **表名：** t_xkcr_investrateelimtmp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [抵销分录模板 xkcr_elimtemp](../xkcr_files/xkcr_elimtemp.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_investrateelimtmp |  | fpkid |
| 2 | idx_xkcr_investrateelimtmp_fb |  | fbasedataid |

---

## 对应调整分录模板-多选基础资料表 t_xkcr_investrateadjtmp

- **表名称：** 对应调整分录模板-多选基础资料表
- **表名：** t_xkcr_investrateadjtmp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [调整分录模板 xkcr_adjustentrytemplate](../xkcr_files/xkcr_adjustentrytemplate.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_investrateadjtmp |  | fpkid |
| 2 | idx_xkcr_investrateadjtmp_fb |  | fbasedataid |
