# 指标库-ipo_quota_info

## 上级指标(归因)-多选基础资料表 t_ipo_dupont_quota

- **表名称：** 上级指标(归因)-多选基础资料表
- **表名：** t_ipo_dupont_quota

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [指标库 ipo_quota_info](../ipobase_files/ipo_quota_info.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipo_dupont_quota |  | fpkid |
| 2 | idx_ipo_dupont_quota |  | fid |

---

## 指标库-多语言表 t_ipo_quota_info_l

- **表名称：** 指标库-多语言表
- **表名：** t_ipo_quota_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 指标名称 | varchar | 50 |  | √ | ' ' | 指标名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipo_quota_info_l |  | fpkid |
| 2 | idx_ipo_quota_info_l |  | fid |

---

## 多指标组合判断-多选基础资料表 t_ipo_base_quota

- **表名称：** 多指标组合判断-多选基础资料表
- **表名：** t_ipo_base_quota

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [指标库 ipo_quota_info](../ipobase_files/ipo_quota_info.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipo_base_quota_0 |  | fid |
| 2 | pk_ipo_base_quota |  | fpkid |

---

## 指标库-主表 t_ipo_quota_info

- **表名称：** 指标库-主表
- **表名：** t_ipo_quota_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [指标分类目录 ipo_quota_type](../ipobase_files/ipo_quota_type.md) |
| 3 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcalculationbasis | 计算依据 | varchar | 50 |  | √ | ' ' | 计算依据,枚举: 0 :财务报表 1 :手工赋值 2 :多指标组合判断 3 :指标 4 :大数据库 5 :财务报表、指标 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | foperationtype | 操作标识 | varchar | 50 |  | √ | ' ' | 操作标识,枚举: 0 :修改 1 :查看 |
| 7 | fformularule | 表达式 | varchar | 500 |  | √ | ' ' | 表达式 |
| 8 | fisportraitmeterhead | 行业画像表头可选指标 | bpchar | 1 |  | √ | '0' | 行业画像表头可选指标 |
| 9 | findicatorscenario | 所属指标场景 | varchar | 50 |  | √ | ' ' | 所属指标场景,枚举: 0 :IPO上市智测 1 :公司财务分析 2 :行业对标分析 3 :专精特新 |
| 10 | fisportraittrendchart | 行业画像趋势图可选指标 | bpchar | 1 |  | √ | '0' | 行业画像趋势图可选指标 |
| 11 | fname | 指标名称 | varchar | 50 |  | √ | ' ' | 指标名称 |
| 12 | ffourclassification | 四级分类 | varchar | 50 |  | √ | ' ' | 四级分类 |
| 13 | fsecondbasicdata | 二级分类基础资料 | int8 | 64 |  | √ | 0 | [指标分类目录 ipo_quota_type](../ipobase_files/ipo_quota_type.md) |
| 14 | fnotcalculate | 不计算情形 | varchar | 50 |  | √ | ' ' | 不计算情形,枚举: 0 :分母为0 2 :分母为负数 1 :分子为负数 |
| 15 | fisenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 16 | frptgroup | 报表项目分组 | varchar | 50 |  | √ | ' ' | 报表项目分组,枚举: |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fformulatranslation | 表达式描述 | varchar | 255 |  | √ | ' ' | 表达式描述 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fproject | 项目 | int8 | 64 |  | √ | 0 | [财务报表项目 ipo_fin_report_item](../ipobase_files/ipo_fin_report_item.md) |
| 21 | ftranexpression | 表达式译文 | varchar | 500 |  | √ | ' ' | 表达式译文 |
| 22 | fisindustryranking | 行业排名"排名指标"可选 | bpchar | 1 |  | √ | '0' | 行业排名"排名指标"可选 |
| 23 | fisdefault | 系统预设 | bpchar | 1 |  | √ | '1' | 系统预设 |
| 24 | fbusinessrelation | 业务相关性 | varchar | 50 |  | √ | ' ' | 业务相关性,枚举: 0 :正相关 1 :负相关 |
| 25 | findustryaverage | 是否可计算行业均值(整体法) | varchar | 50 |  | √ | ' ' | 是否可计算行业均值(整体法),枚举: 0 :是 1 :否 |
| 26 | fformulatranslation_tag | 表达式描述_详情 | text | 0 |  |  | null | 表达式描述_详情 |
| 27 | fsinglequarter | 是否单季度指标 | varchar | 50 |  | √ | ' ' | 是否单季度指标,枚举: 0 :是 1 :否 |
| 28 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 31 | fishardindicators | 硬性指标 | varchar | 50 |  | √ | ' ' | 硬性指标,枚举: 0 :是 1 :否 |
| 32 | fstatisticalmethod | 行业统计方法 | varchar | 50 |  | √ | '1' | 行业统计方法,枚举: 0 :求和 1 :行业均值 |
| 33 | fsecondclassification | 二级分类 | varchar | 50 |  | √ | ' ' | 二级分类 |
| 34 | findicatormeaning | 指标含义 | varchar | 500 |  | √ | ' ' | 指标含义 |
| 35 | ffourbasicdata | 四级分类基础资料 | int8 | 64 |  | √ | 0 | [指标分类目录 ipo_quota_type](../ipobase_files/ipo_quota_type.md) |
| 36 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 38 | ffirstclassification | 一级分类 | varchar | 50 |  | √ | ' ' | 一级分类 |
| 39 | freportvaluetype | 实际报表映射类型 | varchar | 50 |  | √ | ' ' | 实际报表映射类型,枚举: 0 :金额 1 :百分比 2 :是/否 3 :存在/不存在 4 :年/月 |
| 40 | fshowrow | 显示顺序 | int8 | 64 |  | √ | 0 | 显示顺序 |
| 41 | ffirstbasicdata | 一级分类基础资料 | int8 | 64 |  | √ | 0 | [指标分类目录 ipo_quota_type](../ipobase_files/ipo_quota_type.md) |
| 42 | fdatasources | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :公式计算 1 :大数据库 2 :公式计算、大数据库 3 :其他 |
| 43 | faccuracy | 显示精度 | varchar | 50 |  | √ | ' ' | 显示精度,枚举: 0 :0位小数 1 :2位小数 |
| 44 | fisindustryprosperity | 行业景气度X轴、Y轴、面积可选指标 | bpchar | 1 |  | √ | '0' | 行业景气度X轴、Y轴、面积可选指标 |
| 45 | fshowname | 指标显示名称 | varchar | 50 |  | √ | ' ' | 指标显示名称 |
| 46 | fthirdclassification | 三级分类 | varchar | 50 |  | √ | ' ' | 三级分类 |
| 47 | fmetadatacode | 弹窗编码 | varchar | 50 |  | √ | ' ' | 弹窗编码 |
| 48 | fyear | 整数1 | int8 | 64 |  |  | null | 整数1 |
| 49 | fisportraittrendchartyoy | 行业画像趋势图时间轴报告期按同比罗列 | bpchar | 1 |  | √ | '0' | 行业画像趋势图时间轴报告期按同比罗列 |
| 50 | fadapttoroles | 适用角色 | varchar | 50 |  | √ | ' ' | 适用角色,枚举: 0 :全部 1 :总经理/董秘 2 :财务总监 3 :法务总监 4 :中介机构 |
| 51 | funits | 单位 | varchar | 50 |  | √ | ' ' | 单位,枚举: 0 :% 1 :元 2 :天 3 :次 4 :无 5 :个 6 :元/人 7 :年 8 :倍 |
| 52 | fthirdbasicdata | 三级分类基础资料 | int8 | 64 |  | √ | 0 | [指标分类目录 ipo_quota_type](../ipobase_files/ipo_quota_type.md) |
| 53 | fcombofield | 值类型 | varchar | 50 |  | √ | ' ' | 值类型,枚举: 0 :文本 1 :布尔值 2 :数值 3 :小数 4 :整数 5 :日期 6 :长日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipo_quota_info_number |  | fnumber |
| 2 | idx_ipo_quota_info_name |  | fname |
| 3 | pk_ipo_quota_info |  | fid |
