# OMS系统配置-rtecs_omssystem

## 盘点单单据体-子表 t_rtecs_omssys_pd

- **表名称：** 盘点单单据体-子表
- **表名：** t_rtecs_omssys_pd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 6 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtecs_omssys_od_fid |  | fid |
| 2 | pk_rtecs_omssys_pd |  | fentryid |

---

## 入库(采购)单据体-子表 t_rtecs_omssys_purin

- **表名称：** 入库(采购)单据体-子表
- **表名：** t_rtecs_omssys_purin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtecs_omssys_purin |  | fid |
| 2 | pk_rtecs_omssys_purin |  | fentryid |

---

## 原始订单单据体-子表 t_rtecs_omssys_origorder

- **表名称：** 原始订单单据体-子表
- **表名：** t_rtecs_omssys_origorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_origorder |  | fentryid |
| 2 | idx_rtecs_omssys_orig |  | fid |

---

## OMS系统配置-主表 t_rtecs_omssystem

- **表名称：** OMS系统配置-主表
- **表名：** t_rtecs_omssystem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fcorpustype | 集成数据类型 | varchar | 50 |  | √ | ' ' | 集成数据类型,枚举: A :OMS自定义接口 B :奇门自定义接口 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fqimenappkey | 奇门AppKey | varchar | 255 |  | √ | ' ' | 奇门AppKey |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fdefaultpurorgtype | 采购组织取数方式 | varchar | 50 |  | √ | ' ' | 采购组织取数方式,枚举: A :取默认采购组织 B :按库存组织取 C :按供应商映射表取 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fintegrationuser | 集成用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fallowrepeatbill | 重复订单是否落库 | bpchar | 1 |  | √ | ' ' | 重复订单是否落库 |
| 13 | fversionno | 版本号 | varchar | 255 |  | √ | ' ' | 版本号 |
| 14 | fsid | 奇门卖家账户 | varchar | 255 |  | √ | ' ' | 奇门卖家账户 |
| 15 | fqimenappsecret | 奇门AppSecret | varchar | 255 |  | √ | ' ' | 奇门AppSecret |
| 16 | fbasispriceslip | 入库单取价依据 | varchar | 50 |  | √ | 'A' | 入库单取价依据,枚举: A :价税合计 B :含税单价 |
| 17 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 18 | fratetableid | 默认汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 19 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fsecret | AppSecret | varchar | 255 |  | √ | ' ' | AppSecret |
| 21 | fname | 平台名称 | varchar | 50 |  | √ | ' ' | 平台名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fappkey | 奇门接口账户 | varchar | 255 |  | √ | ' ' | 奇门接口账户 |
| 24 | fomssid | 卖家账户（SID） | varchar | 255 |  | √ | ' ' | 卖家账户（SID） |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fdefaultcusttype | 客户取数方式 | varchar | 50 |  | √ | ' ' | 客户取数方式,枚举: A :取默认客户 B :取店铺档案对应客户 |
| 27 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 28 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fsystemversion | 系统版本 | varchar | 255 |  | √ | ' ' | 系统版本 |
| 30 | fomsappkey | AppKey | varchar | 255 |  | √ | ' ' | AppKey |
| 31 | fpurchaseorgid | 默认采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fdefaultunitid | 默认单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fstandardid | 默认分类标准 | int8 | 64 |  | √ | 0 | [物料分类标准 bd_materialgroupstandard](../basedata_files/bd_materialgroupstandard.md) |
| 34 | fouteroms | 集成系统 | varchar | 50 |  | √ | ' ' | 集成系统,枚举: A :旺店通（企业版） B :聚水潭 C :管易云C-ERP数智版 D :吉客云 E :领星 F :旺店通（旗舰版） G :万里牛 |
| 35 | fbatchsource | 批号保质期取数来源 | varchar | 50 |  | √ | 'A' | 批号保质期取数来源,枚举: A :取OMS源单 B :按库存规择匹配 |
| 36 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | furl | 奇门接口地址 | varchar | 255 |  | √ | ' ' | 奇门接口地址 |
| 38 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 39 | fomsurl | 接口地址 | varchar | 255 |  | √ | ' ' | 接口地址 |
| 40 | fdefaultorg | 默认组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fcurrencyid | 默认币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fcustomerid | 默认客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 43 | fdefaultdptid | 默认部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtecs_omssystem_no |  | fnumber |
| 2 | pk_rtecs_omssystem |  | fid |

---

## 跨境售后单单据体-子表 t_rtecs_omssys_kjreturn

- **表名称：** 跨境售后单单据体-子表
- **表名：** t_rtecs_omssys_kjreturn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_kjreturn |  | fentryid |
| 2 | idx_rtecs_sys_kjreturn_fid |  | fid |

---

## 售后退货单据体-子表 t_rtecs_omssys_return

- **表名称：** 售后退货单据体-子表
- **表名：** t_rtecs_omssys_return

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_return |  | fentryid |
| 2 | idx_rtecs_omssys_return |  | fid |

---

## 调拨单单据体-子表 t_rtecs_omssys_trans

- **表名称：** 调拨单单据体-子表
- **表名：** t_rtecs_omssys_trans

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_trans |  | fentryid |
| 2 | idx_rtecs_sys_trans_fid |  | fid |

---

## 入库(其他,调拨,盘盈)单据体-子表 t_rtecs_omssys_stockin

- **表名称：** 入库(其他,调拨,盘盈)单据体-子表
- **表名：** t_rtecs_omssys_stockin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_stockin |  | fentryid |
| 2 | idx_rtecs_omssys_stockin |  | fid |

---

## 出库(其他,调拨,盘亏)单据体-子表 t_rtecs_omssys_stockout

- **表名称：** 出库(其他,调拨,盘亏)单据体-子表
- **表名：** t_rtecs_omssys_stockout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_stockout |  | fentryid |
| 2 | idx_rtecs_omssys_stockout |  | fid |

---

## 组合商品单据体-子表 t_rtecs_omssys_combine

- **表名称：** 组合商品单据体-子表
- **表名：** t_rtecs_omssys_combine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_combine |  | fentryid |
| 2 | idx_rtecs_omssys_combine |  | fid |

---

## 退货入库单据体-子表 t_rtecs_omssys_returnin

- **表名称：** 退货入库单据体-子表
- **表名：** t_rtecs_omssys_returnin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_returnin |  | fentryid |
| 2 | idx_rtecs_omssys_returnin_fk |  | fid |

---

## OMS系统配置-分表 t_rtecs_omssystem_w

- **表名称：** OMS系统配置-分表
- **表名：** t_rtecs_omssystem_w

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwlnappkey | AppKey | varchar | 255 |  | √ | ' ' | AppKey |
| 3 | fwlnsecret | Secret | varchar | 255 |  | √ | ' ' | Secret |
| 4 | fwlnurl | 接口地址 | varchar | 50 |  | √ | ' ' | 接口地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssystem_w |  | fid |

---

## 供货商单据体-子表 t_rtecs_omssys_supplier

- **表名称：** 供货商单据体-子表
- **表名：** t_rtecs_omssys_supplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_supplier |  | fentryid |
| 2 | idx_rtecs_omssys_supplier |  | fid |

---

## 跨境销售订单单据体-子表 t_rtecs_omssys_kjorder

- **表名称：** 跨境销售订单单据体-子表
- **表名：** t_rtecs_omssys_kjorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_kjorder |  | fentryid |
| 2 | idx_rtecs_sys_kjorder_fid |  | fid |

---

## 调拨人单据体-子表 t_rtecs_omssys_transin

- **表名称：** 调拨人单据体-子表
- **表名：** t_rtecs_omssys_transin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtecs_omssys_transin_fid |  | fid |
| 2 | pk_rtecs_omssys_transin |  | fentryid |

---

## OMS系统配置-分表 t_rtecs_omssystem_a

- **表名称：** OMS系统配置-分表
- **表名：** t_rtecs_omssystem_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fallowlossout | 盘亏单 | bpchar | 1 |  | √ | '0' | 盘亏单 |
| 3 | fallowpurchasein | 采购入库单 | bpchar | 1 |  | √ | '0' | 采购入库单 |
| 4 | fallowbranch | 店铺档案 | bpchar | 1 |  | √ | '0' | 店铺档案 |
| 5 | fallowpurchase | 采购订单 | bpchar | 1 |  | √ | '0' | 采购订单 |
| 6 | fallowcombine | 组合商品 | bpchar | 1 |  | √ | '0' | 组合商品 |
| 7 | fallowtrans | 调拨单 | bpchar | 1 |  | √ | '0' | 调拨单 |
| 8 | fallowotherout | 其他出库单 | bpchar | 1 |  | √ | '0' | 其他出库单 |
| 9 | fallowkjreturn | 跨境售后单 | bpchar | 1 |  | √ | '0' | 跨境售后单 |
| 10 | fallowitem | 商品档案 | bpchar | 1 |  | √ | '0' | 商品档案 |
| 11 | fallowkjsalesorder | 跨境销售订单 | bpchar | 1 |  | √ | '0' | 跨境销售订单 |
| 12 | fallowotherin | 其他入库单 | bpchar | 1 |  | √ | '0' | 其他入库单 |
| 13 | fallowpurchaseout | 采购退货单 | bpchar | 1 |  | √ | '0' | 采购退货单 |
| 14 | fallowpd | 盘点单 | bpchar | 1 |  | √ | '0' | 盘点单 |
| 15 | fallowreturn | 售后订单 | bpchar | 1 |  | √ | '0' | 售后订单 |
| 16 | fallowtransin | 调拨入库单 | bpchar | 1 |  | √ | '0' | 调拨入库单 |
| 17 | fallowreturnin | 销售退货入库单 | bpchar | 1 |  | √ | '0' | 销售退货入库单 |
| 18 | fallowtransout | 调拨出库单 | bpchar | 1 |  | √ | '0' | 调拨出库单 |
| 19 | fallowdelivery | 销售出库单 | bpchar | 1 |  | √ | '0' | 销售出库单 |
| 20 | falloworigorder | 平台原始订单 | bpchar | 1 |  | √ | '0' | 平台原始订单 |
| 21 | fallowsalesorder | 销售订单 | bpchar | 1 |  | √ | '0' | 销售订单 |
| 22 | fallowsupplier | 供应商 | bpchar | 1 |  | √ | '0' | 供应商 |
| 23 | fallowsurplusin | 盘盈单 | bpchar | 1 |  | √ | '0' | 盘盈单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssystem_a |  | fid |

---

## 店铺档案单据体-子表 t_rtecs_omssys_branchs

- **表名称：** 店铺档案单据体-子表
- **表名：** t_rtecs_omssys_branchs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_branchs |  | fentryid |
| 2 | idx_rtecs_omssys_branchs |  | fid |

---

## 商品档案单据体-子表 t_rtecs_omssys_items

- **表名称：** 商品档案单据体-子表
- **表名：** t_rtecs_omssys_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_items |  | fentryid |
| 2 | idx_rtecs_omssys_items |  | fid |

---

## OMS系统配置-分表 t_rtecs_omssystem_j

- **表名称：** OMS系统配置-分表
- **表名：** t_rtecs_omssystem_j

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjstappsecret | AppSecret | varchar | 100 |  | √ | ' ' | AppSecret |
| 3 | fjsturl | 接口地址 | varchar | 100 |  | √ | ' ' | 接口地址 |
| 4 | fjstappkey | AppKey | varchar | 100 |  | √ | ' ' | AppKey |
| 5 | ftokengettime | Token获取时间 | timestamp | 0 |  |  | null | Token获取时间 |
| 6 | fisjsttesturl | 是否聚水潭测试环境 | bpchar | 1 |  | √ | '0' | 是否聚水潭测试环境 |
| 7 | ftokenexpires | 剩余有效时间（秒） | int8 | 64 |  | √ | 0 | 剩余有效时间（秒） |
| 8 | fjstaccesstoken | AccessToken | varchar | 100 |  | √ | ' ' | AccessToken |
| 9 | frefreshbetween | token刷新间隔（天） | int8 | 64 |  | √ | 0 | token刷新间隔（天） |
| 10 | fautorefreshtoken | 是否定期刷新token | bpchar | 1 |  | √ | '0' | 是否定期刷新token |
| 11 | fjstrefreshtoken | RefreshToken | varchar | 100 |  | √ | ' ' | RefreshToken |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtecs_omssystem_j |  | fjstappkey |
| 2 | pk_rtecs_omssystem_j |  | fid |

---

## OMS系统配置-分表 t_rtecs_omssystem_k

- **表名称：** OMS系统配置-分表
- **表名：** t_rtecs_omssystem_k

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjacksecret | Secret | varchar | 255 |  | √ | ' ' | Secret |
| 3 | fmemberid | 吉客号 | varchar | 50 |  | √ | ' ' | 吉客号 |
| 4 | fjackappkey | AppKey | varchar | 255 |  | √ | ' ' | AppKey |
| 5 | fjackurl | 接口地址 | varchar | 50 |  | √ | ' ' | 接口地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssystem_k |  | fid |

---

## OMS系统配置-多语言表 t_rtecs_omssystem_l

- **表名称：** OMS系统配置-多语言表
- **表名：** t_rtecs_omssystem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 平台名称 | varchar | 100 |  | √ | ' ' | 平台名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssystem_l |  | fpkid |
| 2 | idx_rtecs_omssystem_l_0 |  | fid,flocaleid |

---

## 销售出库单据体-子表 t_rtecs_omssys_salesout

- **表名称：** 销售出库单据体-子表
- **表名：** t_rtecs_omssys_salesout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtecs_omssys_salesout_fk |  | fid |
| 2 | pk_rtecs_omssys_salesout |  | fentryid |

---

## 调拨出单据体-子表 t_rtecs_omssys_transout

- **表名称：** 调拨出单据体-子表
- **表名：** t_rtecs_omssys_transout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_transout |  | fentryid |
| 2 | idx_rtecs_omssys_transout |  | fid |

---

## OMS系统配置-分表 t_rtecs_omssystem_g

- **表名称：** OMS系统配置-分表
- **表名：** t_rtecs_omssystem_g

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgyappkey | AppKey | varchar | 255 |  | √ | ' ' | AppKey |
| 3 | fgysecret | Secret | varchar | 255 |  | √ | ' ' | Secret |
| 4 | fgysessionkey | SessionKey | varchar | 255 |  | √ | ' ' | SessionKey |
| 5 | fgyurl | 接口地址 | varchar | 255 |  | √ | ' ' | 接口地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtecs_omssystem_g |  | fgyappkey,fgysecret |
| 2 | pk_rtecs_omssystem_g |  | fid |

---

## 盘盈单单据体-子表 t_rtecs_omssys_surplusin

- **表名称：** 盘盈单单据体-子表
- **表名：** t_rtecs_omssys_surplusin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtecs_omsys_surplusin |  | fid |
| 2 | pk_rtecs_omssys_surplusin |  | fentryid |

---

## 采购订单单据体-子表 t_rtecs_omssys_purchase

- **表名称：** 采购订单单据体-子表
- **表名：** t_rtecs_omssys_purchase

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtecs_omssys_purchase |  | fid |
| 2 | pk_rtecs_omssys_purchase |  | fentryid |

---

## 盘亏单单据体-子表 t_rtecs_omssys_surplusout

- **表名称：** 盘亏单单据体-子表
- **表名：** t_rtecs_omssys_surplusout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_surplusout |  | fentryid |
| 2 | idx_rtecs_omsys_surplusout |  | fid |

---

## 出库(采购)单据体-子表 t_rtecs_omssys_purout

- **表名称：** 出库(采购)单据体-子表
- **表名：** t_rtecs_omssys_purout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtecs_omssys_purout |  | fid |
| 2 | pk_rtecs_omssys_purout |  | fentryid |

---

## 销售订单单据体-子表 t_rtecs_omssys_sales

- **表名称：** 销售订单单据体-子表
- **表名：** t_rtecs_omssys_sales

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :) C :)) D :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fleftparens |  | varchar | 50 |  | √ | 'A' | ,枚举: A : B :( C :(( D :((( |
| 5 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :等于 B :不等于 C :在...中 D :不在...中 E :为空 F :不为空 G :包含 H :不包含 I :以...开始 J :以...结束 K :大于 L :小于 M :小于等于 N :大于等于 |
| 9 | fvaluedesc | 值说明 | varchar | 255 |  | √ | ' ' | 值说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flogicfield | 逻辑 | varchar | 50 |  | √ | 'AND' | 逻辑,枚举: AND :并且 OR :或 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtecs_omssys_sales |  | fentryid |
| 2 | idx_rtecs_omssys_sales |  | fid |
