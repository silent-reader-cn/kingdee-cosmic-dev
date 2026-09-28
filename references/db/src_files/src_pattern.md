# 推荐方案-src_pattern

## 标的分录-子表 t_src_patternentry

- **表名称：** 标的分录-子表
- **表名：** t_src_patternentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 权重(%) | numeric | 23 | 10 | √ | 0 | 权重(%) |
| 3 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 4 | fratio | 数量配比 | numeric | 23 | 10 | √ | 0 | 数量配比 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpurlistid | 标的名称 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_patternentry |  | fentryid |
| 2 | idx_src_patternentry_fid |  | fid |

---

## 推荐方案-主表 t_src_pattern

- **表名称：** 推荐方案-主表
- **表名：** t_src_pattern

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fislargezero | 商务价格为0时不参与排名(等同弃标的) | bpchar | 1 |  | √ | '1' | 商务价格为0时不参与排名(等同弃标的) |
| 4 | fscorepara2 | 商务分计算方法β2值 | numeric | 23 | 10 | √ | 2 | 商务分计算方法β2值 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fsuppliernum | 计算平均值时最多取几个供应商 | int4 | 32 |  | √ | 0 | 计算平均值时最多取几个供应商 |
| 8 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 9 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 10 | fbasescoreratio2 | 评标基准价系数(%) | numeric | 19 | 6 | √ | 0 | 评标基准价系数(%) |
| 11 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | fcalcratio | 中标占比计算插件 | varchar | 100 |  | √ | ' ' | 中标占比计算插件 |
| 13 | fcalcanaly | 自定义字段值计算插件 | varchar | 100 |  | √ | ' ' | 自定义字段值计算插件 |
| 14 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 15 | fisnonnegative | 商务得分是否必须大于或等于零 | bpchar | 1 |  | √ | '0' | 商务得分是否必须大于或等于零 |
| 16 | fbasescore | 基准得分(满分) | numeric | 19 | 6 | √ | 0 | 基准得分(满分) |
| 17 | fisbydecision | 根据标的定标金额计算定标金额汇总 | bpchar | 1 |  | √ | '0' | 根据标的定标金额计算定标金额汇总 |
| 18 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fruleassess | 商务报价计算规则(招标) | bpchar | 1 |  | √ | ' ' | 商务报价计算规则(招标),枚举: 1 :标的单价 2 :报价包的采购总金额 3 :报价包内所有产品的平均价 4 :其他 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 22 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 23 | fscoreformula | 商务分计算方法 | varchar | 1 |  | √ | ' ' | 商务分计算方法,枚举: 1 :基准价/投标价*100 或 投标价/基准价*100 2 :商务基准得分-[abs(投标价-基准价)/基准价]*β*100 |
| 24 | fsuppliernum2 | 去掉最高值最低值的计算基数 | int4 | 32 |  | √ | 0 | 去掉最高值最低值的计算基数 |
| 25 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 26 | fvaluefield | 商务价格的取值来源 | varchar | 255 |  | √ | ' ' | 商务价格的取值来源,枚举: amount :未税金额 taxamount :含税金额 price :未税单价 taxprice :含税单价 discount :折扣率(%) rebate :返点(%) decrease :降幅(%) feerate :费率(%) vieamount :竞价金额 pkgtaxamount :标段含税金额 pkgamount :标段未税金额 calcvalue :自定义字段 locprice :本币未税单价 loctaxprice :本币含税单价 locamount :本币未税金额 loctaxamount :本币含税金额 |
| 27 | fwinruleid | 中标原则 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 28 | fminscoreratio | 最低商务得分比率(%) | numeric | 23 | 10 | √ | 0 | 最低商务得分比率(%) |
| 29 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 32 | favgtype | 平均值计算方式 | bpchar | 1 |  | √ | ' ' | 平均值计算方式,枚举: 1 :不取平均值 2 :按标的行数计算平均值 3 :按标的数量计算平均值 |
| 33 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 34 | franktype | 价格排名方式 | bpchar | 1 |  | √ | ' ' | 价格排名方式,枚举: 1 :最低值排名 2 :最高值排名 3 :平均值排名 4 :随机排名(随机抽取) 5 :基准值(起标价) 6 :基准值(平均价) |
| 35 | fcalctotal | 金额汇总计算插件 | varchar | 100 |  | √ | ' ' | 金额汇总计算插件 |
| 36 | fbasescoreratio | 基准商务得分比率(%) | numeric | 23 | 10 | √ | 0 | 基准商务得分比率(%) |
| 37 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 3 :按标的 |
| 38 | fsumtype | 商务得分汇总维度 | bpchar | 1 |  | √ | ' ' | 商务得分汇总维度,枚举: 1 :按供应商汇总 2 :按供应商+标段汇总 3 :按供应商+标段+标的汇总 |
| 39 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fremark | 方案描述 | varchar | 255 |  | √ | ' ' | 方案描述 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fprojectd | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 45 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 46 | fvietype | 竞价类型 | bpchar | 1 |  | √ | ' ' | 竞价类型,枚举: A :降价(反向拍卖) B :加价(正向拍卖) |
| 47 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 48 | fcalcrank | 排名推荐计算插件 | varchar | 100 |  | √ | ' ' | 排名推荐计算插件 |
| 49 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 50 | fscorepara | 商务分计算方法β1值 | numeric | 19 | 6 | √ | 1 | 商务分计算方法β1值 |
| 51 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | fratiotype | 配比与权重设置方式 | bpchar | 1 |  | √ | ' ' | 配比与权重设置方式,枚举: 1 :按项目设置 2 :按标段设置 3 :按标的设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_src_pattern_createorg |  | fcreateorgid |
| 2 | idx_src_pattern_fcreatetime |  | fcreatetime |
| 3 | idx_src_pattern_fwinruleid |  | fwinruleid |
| 4 | idx_src_pattern_fmasterid |  | fmasterid |
| 5 | idx_src_pattern_fruleassesidxs |  | fruleassess |
| 6 | pk_src_pattern |  | fid |
| 7 | idx_src_pattern_fnumber |  | fnumber |
| 8 | idx_src_pattern_fprojectd |  | fprojectd |
| 9 | idx_t_src_pattern_master |  | fmasterid |

---

## 推荐方案-使用范围表 t_src_pattern_u

- **表名称：** 推荐方案-使用范围表
- **表名：** t_src_pattern_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_src_pattern_u |  | fdataid,fuseorgid |
| 2 | idx_t_src_pattern_u_uo |  | fuseorgid |

---

## 推荐方案-使用范围位图表 t_src_pattern_m

- **表名称：** 推荐方案-使用范围位图表
- **表名：** t_src_pattern_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_src_pattern_m |  | forgid |

---

## 推荐方案-多语言表 t_src_pattern_l

- **表名称：** 推荐方案-多语言表
- **表名：** t_src_pattern_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_pattern_l_id |  | fid,flocaleid |
| 2 | pk_src_pattern_l |  | fpkid |

---

## 寻源方式-多选基础资料表 t_src_patternsourcetype

- **表名称：** 寻源方式-多选基础资料表
- **表名：** t_src_patternsourcetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_patternsourcetype_fid |  | fid |
| 2 | pk_src_patternsourcetype |  | fpkid |

---

## 参数分录-子表 t_src_patternparams

- **表名称：** 参数分录-子表
- **表名：** t_src_patternparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 默认值 | varchar | 512 |  | √ | ' ' | 默认值 |
| 3 | fparameterid | 参数编码 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 4 | fparamname | fparamname | varchar | 50 |  | √ | ' ' |  |
| 5 | fbasedatainfo | 参数说明 | varchar | 512 |  | √ | ' ' | 参数说明 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fismust | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 8 | fparamtype | fparamtype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_patternparams_fid |  | fid |
| 2 | pk_src_patternparams |  | fentryid |
