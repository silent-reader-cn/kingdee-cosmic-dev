# 报表项目-pa_reportitem

## 报表项目-多语言表 t_pa_reportitem_l

- **表名称：** 报表项目-多语言表
- **表名：** t_pa_reportitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_reportitem_l_fid |  | fid |
| 2 | pk_t_pa_reportitem_l |  | fpkid |

---

## 公式依赖报表项-子表 t_pa_reportitem_dep

- **表名称：** 公式依赖报表项-子表
- **表名：** t_pa_reportitem_dep

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemnumber | 依赖报表项编码 | varchar | 80 |  | √ | ' ' | 依赖报表项编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_reportitem_dep |  | fentryid |
| 2 | idx_pa_reportdep_1 |  | fid |
| 3 | idx_pa_reportdep_2 |  | fitemnumber |

---

## 报表项目-主表 t_pa_reportitem

- **表名称：** 报表项目-主表
- **表名：** t_pa_reportitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 报表项目类型 | int8 | 64 |  | √ | 0 | [报表项目类型 pa_reportitemtype](../pa_files/pa_reportitemtype.md) |
| 5 | fisleaf | 明细报表项 | bpchar | 1 |  | √ | '1' | 明细报表项 |
| 6 | fcomptype | 计算依据 | bpchar | 1 |  | √ | '0' | 计算依据,枚举: 0 :按维度计算 1 :按报表项目计算 |
| 7 | fformulacom | 公式转码后用于计算 | varchar | 255 |  | √ | ' ' | 公式转码后用于计算 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fformuladesc_tag | 公式描述_详情 | text | 0 |  |  | null | 公式描述_详情 |
| 10 | fformulacom_tag | 公式转码后用于计算_详情 | text | 0 |  |  | null | 公式转码后用于计算_详情 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fformuladesc | 公式描述 | varchar | 255 |  | √ | ' ' | 公式描述 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fparent | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 17 | fformula | 公式 | varchar | 255 |  | √ | ' ' | 公式 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fformula_tag | 公式_详情 | text | 0 |  |  | null | 公式_详情 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_reportitem |  | fid |
| 2 | idx_pa_reportitem_ngc |  | fnumber,fgroupid,fcomptype |
| 3 | idx_pa_reportitem_gc |  | fgroupid,fcomptype |
