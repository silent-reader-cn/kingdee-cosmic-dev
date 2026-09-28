# 计划订单-mrp_planorder

## 单据体-子表 t_mrp_planorderentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_planorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequiredate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 3 | fentryreplacematerial | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 4 | frequireqty | 基本单位需求数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位需求数量 |
| 5 | fwastagerateformula | 损耗计算公式 | varchar | 30 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 6 | fstandqty | 基本单位标准用量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位标准用量 |
| 7 | fissuemode | 领送料方式 | varchar | 30 |  | √ | '11010' | 领送料方式,枚举: 11010 :生产领料 11040 :不领料 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率% |
| 10 | fbizrequireqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 11 | fbizqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0 | 用量：分母 |
| 12 | freplacegroup | 替代组号 | int4 | 32 |  | √ | 0 | 替代组号 |
| 13 | fbomid | BOM表头ID | int8 | 64 |  | √ | 0 | BOM表头ID |
| 14 | fentryreplaceplan | 替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |
| 15 | fbizlossqty | 损耗数量 | numeric | 23 | 10 | √ | 0 | 损耗数量 |
| 16 | fownertype | 货主类型 | varchar | 30 |  | √ | 'bos_org' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 17 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | '0' | 跳层 |
| 18 | fbizdroprequireqty | 已投放需求数量 | numeric | 23 | 10 | √ | 0 | 已投放需求数量 |
| 19 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 20 | fentryauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 21 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 22 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 23 | fbizunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fqtydenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分母 |
| 25 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | fentrydroprequireqty | 基本单位已投放需求数量 | numeric | 23 | 10 | √ | 0 | 基本单位已投放需求数量 |
| 27 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 28 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 29 | fissueorgid | 发料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 31 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fentryrepqty | 替代数量 | numeric | 23 | 10 | √ | 0 | 替代数量 |
| 33 | foutorgid | 调出组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fentryreplacestra | 替代策略 | varchar | 30 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | flossqty | 基本单位损耗数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位损耗数量 |
| 38 | fbizstandqty | 标准用量 | numeric | 23 | 10 | √ | 0 | 标准用量 |
| 39 | fentryisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 40 | fsupplytype | 供应类型 | varchar | 60 |  | √ | ' ' | 供应类型,枚举: 10910 :本库存组织领料 10920 :跨库存组织调拨 10930 :跨库存组织领料 10940 :跨库存组织直送 |
| 41 | fiskey | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 42 | fmaterialid | 子项编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 43 | fentryconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 44 | fentryreplacepriority | 替代优先级 | int4 | 32 |  | √ | 0 | 替代优先级 |
| 45 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 46 | fmode | 行标识 | varchar | 60 |  | √ | ' ' | 行标识,枚举: A :手工新增 B :BOM展开新增 |
| 47 | fleadtime | 提前期偏置时间(天) | int4 | 32 |  | √ | 0 | 提前期偏置时间(天) |
| 48 | foutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 49 | fqtytype | 用量类型 | varchar | 60 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 50 | fqtynumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分子 |
| 51 | fbizqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0 | 用量：分子 |
| 52 | fentryreplacemethod | 替代方式 | varchar | 30 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 |
| 53 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 54 | ftype | 子项类型 | varchar | 30 |  | √ | ' ' | 子项类型,枚举: A :库存 B :物料组 C :文本 D :设备 E :工具 |
| 55 | flocationid | 发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 56 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 57 | fisstockalloc | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 58 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 59 | fentryrepmaterials | 替代物料 | varchar | 512 |  | √ | ' ' | 替代物料 |
| 60 | fisbackflushnew | 倒冲 | varchar | 30 |  | √ | 'A' | 倒冲,枚举: A :不倒冲 B :始终倒冲 |
| 61 | fentrymaterialplanid | 物料计划信息 | int8 | 64 |  | √ | 0 | 物料计划信息 mpdm_materialplan |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planorderentry |  | fid,fseq |
| 2 | t_mrp_planorderentry_pkey |  | fentryid |

---

## 联副产品-子表 t_mrp_planordercopentry

- **表名称：** 联副产品-子表
- **表名：** t_mrp_planordercopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcopentrytype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 10720 :联产品 10730 :副产品 |
| 3 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | fbizcopyallqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 5 | fbizcopyqty | 单位数量 | numeric | 23 | 10 | √ | 0 | 单位数量 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcopentryauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fcopentryallqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 9 | fbizcopyunitid | 产品计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fcopentryversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 11 | fcopentryoperation | 产出工序 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 12 | fcopentrymaterial | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 13 | fcopentryvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fcopentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fcopentryqty | 基本单位单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位单位数量 |
| 16 | fcopentryunit | 产品基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fcopentryinvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 20 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_planordercopentry |  | fentryid |
| 2 | idx_mrp_planordercopentry_fid |  | fid |

---

## 单据体-分表 t_mrp_planorderentry_c

- **表名称：** 单据体-分表
- **表名：** t_mrp_planorderentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcmplsetplan | fcmplsetplan | int8 | 64 |  | √ | 0 |  |
| 3 | fsmulatoccup | fsmulatoccup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fcmplstdmdnum | fcmplstdmdnum | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fbomexpandpath | bom展开路径 | varchar | 500 |  | √ | ' ' | bom展开路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planorderentry_c |  | fid |
| 2 | pk_mrp_planorderentry_c |  | fentryid |

---

## 联副产品-多语言表 t_mrp_planordercopentry_l

- **表名称：** 联副产品-多语言表
- **表名：** t_mrp_planordercopentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcopentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
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
| 1 | pk_mrp_planordercopentry_l |  | fpkid |
| 2 | idx_mrp_planordercopentry_l_el |  | fentryid,flocaleid |

---

## 计划订单-主表 t_mrp_planorder

- **表名称：** 计划订单-主表
- **表名：** t_mrp_planorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanprogram | 计划方案 | int8 | 64 |  | √ | 0 | 计划方案 mrp_planscheme |
| 3 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 4 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fyield | 成品率% | numeric | 23 | 10 | √ | 0.0000000000 | 成品率% |
| 8 | fdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 9 | fenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 10 | fdemandseq | 需求单据分录行号 | int4 | 32 |  | √ | 0 | 需求单据分录行号 |
| 11 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fismrpcal | 已计划运算 | bpchar | 1 |  | √ | '0' | 已计划运算 |
| 13 | fordertype | 订单类型 | varchar | 60 |  | √ | ' ' | 订单类型,枚举: 10030 :自制 10050 :委外 10040 :外购 |
| 14 | fownertype | 货主类型 | varchar | 30 |  | √ | 'bos_org' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 15 | fmaterial | 物料主档 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 16 | fplantags | 计划标识 | int8 | 64 |  | √ | 0 | 计划标识 mpdm_plantag |
| 17 | fadvisedroptime | 建议投放时间 | timestamp | 0 |  |  | null | 建议投放时间 |
| 18 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 19 | fmateriallock | 订单物料锁定 | bpchar | 1 |  | √ | '0' | 订单物料锁定 |
| 20 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 21 | fqty | 基本单位本次投放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位本次投放数量 |
| 22 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 23 | fbizunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fbillstatus | 单据状态 | varchar | 60 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | forderdate | 计划准备日期 | timestamp | 0 |  |  | null | 计划准备日期 |
| 26 | fdroptime | 投放时间 | timestamp | 0 |  |  | null | 投放时间 |
| 27 | fdropbilltypeid | 投放单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 28 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 29 | fplanoperatenum2 | 计划运算号2 | int8 | 64 |  | √ | 0 | 运算日志 mrp_caculate_log |
| 30 | fthreestock | 三品库存 | numeric | 23 | 10 | √ | 0.0000000000 | 三品库存 |
| 31 | fkittingbaseqty | 齐套基本数量 | numeric | 23 | 10 | √ | 0 | 齐套基本数量 |
| 32 | fplanpersonid | 计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fordermoq | 最小订单量 | numeric | 23 | 10 | √ | 0.0000000000 | 最小订单量 |
| 34 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fcommentreason | 备注原因 | varchar | 30 |  | √ | ' ' | 备注原因,枚举: a :SOP变化 b :独立需求未及时录入 c :BOM未归档 d :EC变更或物料替代 e :故障品不参与排产 f :其他原因 |
| 36 | fdemandtype | fdemandtype | varchar | 50 |  | √ | ' ' |  |
| 37 | fbom | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 38 | fstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 39 | fbizorderqty | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 40 | fdatasource | 数据来源 | varchar | 60 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :计算产生 C :拆分产生 D :合并产生 |
| 41 | fmateriallmft | 物料生产信息 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | funit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 44 | fdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 45 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 46 | fishistory | 是否历史数据 | bpchar | 1 |  | √ | '0' | 是否历史数据 |
| 47 | fbizdropqty | 投放数量 | numeric | 23 | 10 | √ | 0 | 投放数量 |
| 48 | fdropqty | 基本单位投放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位投放数量 |
| 49 | fproorpurorg | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 50 | fmaterialspread | 重新展算订单物料 | bpchar | 1 |  | √ | '0' | 重新展算订单物料 |
| 51 | fendproqty | 基本单位成品数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位成品数量 |
| 52 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | finwardept | 入库组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 54 | fhistorydate | 历史日期 | timestamp | 0 |  |  | null | 历史日期 |
| 55 | fschedule | 投放失败原因 | varchar | 500 |  | √ | ' ' | 投放失败原因 |
| 56 | forderqty | 基本单位订单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位订单数量 |
| 57 | favailabledate | 可用日期 | timestamp | 0 |  |  | null | 可用日期 |
| 58 | fplanoperatenum | 计划运算号 | varchar | 100 |  | √ | ' ' | 计划运算号 |
| 59 | fbasedemandqty | 基本单位净需求数量 | numeric | 23 | 10 | √ | 0 | 基本单位净需求数量 |
| 60 | fmaterialattr | 物料属性 | varchar | 60 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 |
| 61 | fmaterialplanid | 物料编码 | int8 | 64 |  | √ | 0 | 物料计划信息 mpdm_materialplan |
| 62 | fremark | fremark | varchar | 50 |  | √ | ' ' |  |
| 63 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 64 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 65 | fismpsonly | 只算MPS | bpchar | 1 |  | √ | '0' | 只算MPS |
| 66 | fecnversion | ECN版本 | int8 | 64 |  | √ | 0 | ECN版本 pdm_ecnversion |
| 67 | fsurplusdropqty | 基本单位剩余待投放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位剩余待投放数量 |
| 68 | fdemandbill | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 69 | fplantag | fplantag | varchar | 60 |  | √ | ' ' |  |
| 70 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :正常 B :关闭 C :拆分关闭 D :合并关闭 E :投放关闭 |
| 71 | funfoldbomdate | 展开BOM时间 | timestamp | 0 |  |  | null | 展开BOM时间 |
| 72 | dropstatus | dropstatus | varchar | 30 |  | √ | ' ' |  |
| 73 | fdropstatus | 投放状态 | varchar | 30 |  | √ | ' ' | 投放状态,枚举: A :未投放 B :投放中 C :部分投放 D :已投放 E :投放失败 |
| 74 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 75 | fbizendproqty | 成品数量 | numeric | 23 | 10 | √ | 0 | 成品数量 |
| 76 | fdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planorder_ma |  | fmaterial |
| 2 | idx_mrp_planorder_pl |  | fplanoperatenum |
| 3 | idx_mrp_planorder_fnum |  | fbillno |
| 4 | idx_mrp_planorder_tracknumber |  | ftracknumber |
| 5 | t_mrp_planorder_pkey |  | fid |
| 6 | idx_mrp_planorder_org |  | fproorpurorg |

---

## 关联子实体-子表 t_mrp_planorder_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mrp_planorder_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mrp_planorder_lk_pkey |  | fpkid |
| 2 | idx_mrp_planorder_lk_fk |  | fid |

---

## 计划订单-关联追踪表 t_mrp_planorder_tc

- **表名称：** 计划订单-关联追踪表
- **表名：** t_mrp_planorder_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planorder_tc_tbill |  | ftbillid |
| 2 | t_mrp_planorder_tc_pkey |  | fid |
| 3 | idx_mrp_planorder_tc_tid |  | ftid |

---

## 计划订单-多语言表 t_mrp_planorder_l

- **表名称：** 计划订单-多语言表
- **表名：** t_mrp_planorder_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 原因描述 | varchar | 512 |  | √ | ' ' | 原因描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_planorder_l |  | fpkid |
| 2 | idx_mrp_planorder_l |  | fid,flocaleid |

---

## 计划订单-反写记录表 t_mrp_planorder_wb

- **表名称：** 计划订单-反写记录表
- **表名：** t_mrp_planorder_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planorder_wb_fk |  | fid |
| 2 | t_mrp_planorder_wb_pkey |  | fentryid |
