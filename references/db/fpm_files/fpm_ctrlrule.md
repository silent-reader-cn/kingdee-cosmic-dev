# 计划控制规则-fpm_ctrlrule

## 控制单据单据体-子表 t_fpm_ctrlbill

- **表名称：** 控制单据单据体-子表
- **表名：** t_fpm_ctrlbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fctrltime | 计划执行类型 | varchar | 50 |  | √ | ' ' | 计划执行类型,枚举: 1 :申请占用 2 :计划执行 3 :执行冲回 |
| 3 | fbilldatesmp | 单据日期短字段 | varchar | 50 |  | √ | ' ' | 单据日期短字段 |
| 4 | fmbillcurrency | billcurrency多语言文本 | varchar | 255 |  | √ | ' ' | billcurrency多语言文本 |
| 5 | fmbilldate | billdate多语言文本 | varchar | 255 |  | √ | ' ' | billdate多语言文本 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbilldate | 单据日期 | varchar | 255 |  | √ | ' ' | 单据日期 |
| 8 | fmbillorg | billorg多语言文本 | varchar | 255 |  | √ | ' ' | billorg多语言文本 |
| 9 | ftextfield | 单据状态字段 | varchar | 50 |  | √ | ' ' | 单据状态字段 |
| 10 | fbillorgsmp | 业务组织来源短字段 | varchar | 50 |  | √ | ' ' | 业务组织来源短字段 |
| 11 | fallsinglefilter | 生效条件字段名称 | varchar | 1000 |  | √ | ' ' | 生效条件字段名称 |
| 12 | fcurbillformnum | 当前单据分录编码 | int8 | 64 |  | √ | 0 | 当前单据分录编码 |
| 13 | fbillcurrency | 单据币种 | varchar | 255 |  | √ | ' ' | 单据币种 |
| 14 | fbilldeptkey | 部门来源字段 | varchar | 50 |  | √ | ' ' | 部门来源字段 |
| 15 | fremarkfieldkey | 备注信息字段 | varchar | 1000 |  | √ | ' ' | 备注信息字段 |
| 16 | fmremarkfield | remarkfield多语言文本 | varchar | 1000 |  | √ | ' ' | remarkfield多语言文本 |
| 17 | fmeffectname | effectname多语言文本 | varchar | 255 |  | √ | ' ' | effectname多语言文本 |
| 18 | fbillcurrencysmp | 币种短字段 | varchar | 50 |  | √ | ' ' | 币种短字段 |
| 19 | fbilldeptsmp | 部门来源短字段 | varchar | 50 |  | √ | ' ' | 部门来源短字段 |
| 20 | fremarkfieldsmp | 备注信息短字段 | varchar | 1000 |  | √ | ' ' | 备注信息短字段 |
| 21 | fbilldept | 部门来源 | varchar | 255 |  | √ | ' ' | 部门来源 |
| 22 | fbillform | 控制单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 23 | fbillcurrencykey | 币种字段 | varchar | 50 |  | √ | ' ' | 币种字段 |
| 24 | fbillorgkey | 业务组织来源字段 | varchar | 50 |  | √ | ' ' | 业务组织来源字段 |
| 25 | fmbilldept | billdept多语言文本 | varchar | 255 |  | √ | ' ' | billdept多语言文本 |
| 26 | ffilterrows | 生效条件JSON | varchar | 1000 |  | √ | ' ' | 生效条件JSON |
| 27 | fremarkfield | 备注信息 | varchar | 1000 |  | √ | ' ' | 备注信息 |
| 28 | feffectkey | 生效条件Sql | varchar | 1000 |  | √ | ' ' | 生效条件Sql |
| 29 | feffectname | 生效条件 | varchar | 255 |  | √ | ' ' | 生效条件 |
| 30 | fprebillformnum | 上游受控单据 | varchar | 50 |  | √ | ' ' | 上游受控单据,枚举: |
| 31 | fwritebacktiming | 反写时机 | varchar | 50 |  | √ | ' ' | 反写时机,枚举: save :保存 submit :提交 |
| 32 | fbillorg | 编报组织 | varchar | 255 |  | √ | ' ' | 编报组织 |
| 33 | fbilldatekey | 单据日期字段 | varchar | 50 |  | √ | ' ' | 单据日期字段 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fratetype | 汇率类型 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 36 | fallsinglefilter_tag | 生效条件字段名称_详情 | text | 0 |  |  | null | 生效条件字段名称_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpm_ctrlbill |  | fentryid |
| 2 | idx_fpm_ctrlbill_fk |  | fid |

---

## 计划控制规则-主表 t_fpm_ctrlrule

- **表名称：** 计划控制规则-主表
- **表名：** t_fpm_ctrlrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [资金计划控制规则分组 fpm_ctrlrulegroup](../fpm_files/fpm_ctrlrulegroup.md) |
| 3 | fctrlruleeffect | 生效条件 | varchar | 2000 |  | √ | ' ' | 生效条件 |
| 4 | fctrlcurrency | 控制币种 | varchar | 50 |  | √ | ' ' | 控制币种,枚举: |
| 5 | fctrlcycle | 控制周期 | varchar | 50 |  | √ | ' ' | 控制周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbyperiod | 按 | varchar | 50 |  | √ | ' ' | 按,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 8 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 9 | fiscycletotal | 按大周期汇总控制 | bpchar | 1 |  | √ | '0' | 按大周期汇总控制 |
| 10 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fctrlpolicy | 控制方式 | varchar | 50 |  | √ | ' ' | 控制方式,枚举: 2 :实际数小于等于预算数 4 :实际数小于预算数 1 :实际数大于等于预算数 3 :实际数大于预算数 |
| 12 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 13 | fpasswhennull | 计划数为空时通过 | bpchar | 1 |  | √ | '1' | 计划数为空时通过 |
| 14 | fctrlorgsum | fctrlorgsum | bpchar | 1 |  | √ | '0' |  |
| 15 | fisperiodcumctrl | 年内按期累计控制 | bpchar | 1 |  | √ | '0' | 年内按期累计控制 |
| 16 | fdescription | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 17 | fwizardscheme | 预算数来源 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 18 | fbgcurrency | 控制本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | factsource | 实际数来源 | varchar | 50 |  | √ | ' ' | 实际数来源,枚举: 1 :仅单据 2 :单据及实际数报表 3 :仅实际数报表 |
| 20 | fisyearcumctrl | 跨年按期累计控制 | bpchar | 1 |  | √ | '0' | 跨年按期累计控制 |
| 21 | fisyearsumctrl | 跨年汇总控制 | bpchar | 1 |  | √ | '0' | 跨年汇总控制 |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fwarptype | 偏差方式 | varchar | 50 |  | √ | ' ' | 偏差方式,枚举: 1 :偏差率（%） 2 :偏差额 |
| 25 | fcounttype | 统计方式 | varchar | 50 |  | √ | ' ' | 统计方式,枚举: 1 :汇总 2 :以实际数报表为准 |
| 26 | fcalcpolicy | 计算方式 | varchar | 50 |  | √ | ' ' | 计算方式,枚举: 1 :首记录 2 :最大值 3 :最小值 4 :平均值 5 :末记录 |
| 27 | fruletype | 控制规则类型 | varchar | 50 |  | √ | ' ' | 控制规则类型,枚举: 0 :普通 1 :动态 |
| 28 | fiscalcbillback | 申请占用释放（下游单据反写字段） | bpchar | 1 |  | √ | '0' | 申请占用释放（下游单据反写字段） |
| 29 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 32 | fwarptypeprice | 偏差方式 | varchar | 50 |  | √ | ' ' | 偏差方式,枚举: 1 :偏差率（%） 2 :偏差额 |
| 33 | fvirtuallywriteback | 虚拟反写 | bpchar | 1 |  | √ | '0' | 虚拟反写 |
| 34 | fctrlruleeffectsql | 生效条件sql | varchar | 2000 |  | √ | ' ' | 生效条件sql |
| 35 | fiscalcbill | 单据字段 | bpchar | 1 |  | √ | '0' | 单据字段 |
| 36 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 37 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 39 | fcurrency | 币种 | varchar | 50 |  | √ | ' ' | 币种,枚举: |
| 40 | fpasswhennomapping | 费用项目无成本子要素对应关系通过 | bpchar | 1 |  | √ | '1' | 费用项目无成本子要素对应关系通过 |
| 41 | fcontroltype | 控制方式 | varchar | 50 |  | √ | ' ' | 控制方式,枚举: 2 :实际数小于等于预算数 4 :实际数小于预算数 1 :实际数大于等于预算数 3 :实际数大于预算数 |
| 42 | fexectitle | 计划执行进度提示百分比（%） | numeric | 23 | 10 | √ | 0 | 计划执行进度提示百分比（%） |
| 43 | fmulcombofield | fmulcombofield | varchar | 50 |  | √ | ' ' |  |
| 44 | fwarpvalueprice | 偏差值 | numeric | 23 | 10 | √ | 0 | 偏差值 |
| 45 | fctrlruleeffectjson | 生效条件JSON | varchar | 2000 |  | √ | ' ' | 生效条件JSON |
| 46 | fshowbggroup | 计划执行按钮组 | varchar | 50 |  | √ | ' ' | 计划执行按钮组,枚举: |
| 47 | fwarpvalue | 偏差值 | numeric | 23 | 10 | √ | 0 | 偏差值 |
| 48 | fmainplantpl | 计划模板 | int8 | 64 |  | √ | 0 | [资金计划模板 fpm_mainplantemplate](../fpm_files/fpm_mainplantemplate.md) |
| 49 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 50 | fisshow | 未超额提示 | bpchar | 1 |  | √ | '0' | 未超额提示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_fnumber |  | fnumber |
| 2 | pk_fpm_ctrlrule |  | fid |

---

## 控制维度单据体-子表 t_fpm_ctrldim

- **表名称：** 控制维度单据体-子表
- **表名：** t_fpm_ctrldim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fctrldimension | 控制维度 | varchar | 500 |  |  | ' ' | 控制维度,枚举: bizunit :业务单元 currency :币种 dept :部门 project :项目 settletype :结算方式 customer :客户 supplier :供应商 expense :费用项目 material :物料 materialgroup :物料分类 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | ffundusage | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_ctrldim_fk |  | fid |
| 2 | pk_fpm_ctrldim |  | fentryid |

---

## 控制操作与强度单据体-子表 t_fpm_ctrlbilloprate

- **表名称：** 控制操作与强度单据体-子表
- **表名：** t_fpm_ctrlbilloprate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fctrllevel | 控制强度 | varchar | 50 |  | √ | ' ' | 控制强度,枚举: 1 :不控制 2 :提示 3 :强制 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fctrloprate | 操作 | varchar | 50 |  | √ | ' ' | 操作,枚举: submit :提交 audit :审核 unsubmit :撤销 unaudit :反审核 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpm_ctrlbilloprate |  | fdetailid |
| 2 | idx_fpm_ctrlbilloprate_fk |  | fentryid |

---

## 控制维度子单据体-多语言表 t_fpm_ctrlbilldim_l

- **表名称：** 控制维度子单据体-多语言表
- **表名：** t_fpm_ctrlbilldim_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmbilldimensionfield | billdimensionfield多语言文本 | varchar | 255 |  | √ | ' ' | billdimensionfield多语言文本 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpm_ctrlbilldim_l |  | fpkid |
| 2 | idx_fpm_ctrlbilldim_l |  | fdetailid,flocaleid |

---

## 控制数据子单据体-子表 t_fpm_ctrlbilldata

- **表名称：** 控制数据子单据体-子表
- **表名：** t_fpm_ctrlbilldata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbilldatafieldkey | 单据字段KEY | varchar | 50 |  | √ | ' ' | 单据字段KEY |
| 2 | fmbillwritebackfield | billwritebackfield多语言文本 | varchar | 255 |  | √ | ' ' | billwritebackfield多语言文本 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbilldatafield | 单据字段 | varchar | 255 |  | √ | ' ' | 单据字段 |
| 5 | fbillwritebackformula | 下游单据计算公式 | varchar | 2000 |  | √ | ' ' | 下游单据计算公式 |
| 6 | fbilldatafieldsmp | 单据短字段 | varchar | 50 |  | √ | ' ' | 单据短字段 |
| 7 | fmbilldatafield | billdatafield多语言文本 | varchar | 255 |  | √ | ' ' | billdatafield多语言文本 |
| 8 | fprebillfield | 反写上游单据字段 | varchar | 50 |  | √ | ' ' | 反写上游单据字段 |
| 9 | fprebillfieldkey | 反写上游单据长字段 | varchar | 50 |  | √ | ' ' | 反写上游单据长字段 |
| 10 | fbillwritebackfieldkey | 申请占用释放字段 | varchar | 50 |  | √ | ' ' | 申请占用释放字段 |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fbillwritebackfield | 申请占用释放 | varchar | 255 |  | √ | ' ' | 申请占用释放 |
| 13 | fbillwritebackfieldsmp | 申请占用释放短字段 | varchar | 50 |  | √ | ' ' | 申请占用释放短字段 |
| 14 | fprebillfieldsmp | 反写上游单据短字段 | varchar | 50 |  | √ | ' ' | 反写上游单据短字段 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | fbilldatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpm_ctrlbilldata |  | fdetailid |
| 2 | idx_fpm_ctrlbilldata_fk |  | fentryid |

---

## 计划控制规则-多语言表 t_fpm_ctrlrule_l

- **表名称：** 计划控制规则-多语言表
- **表名：** t_fpm_ctrlrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpm_ctrlrule_l |  | fpkid |
| 2 | idx_fpm_ctrlrule_l |  | fid,flocaleid |

---

## 适用范围单据体-子表 t_fpm_ctrlruleorg

- **表名称：** 适用范围单据体-子表
- **表名：** t_fpm_ctrlruleorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fctrlorg | 受控组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_ctrlruleorg_fk |  | fid |
| 2 | pk_fpm_ctrlruleorg |  | fentryid |

---

## 控制维度子单据体-子表 t_fpm_ctrlbilldim

- **表名称：** 控制维度子单据体-子表
- **表名：** t_fpm_ctrlbilldim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdimensionformid | 维度业务对象ID | varchar | 50 |  | √ | ' ' | 维度业务对象ID |
| 2 | fmbilldimensionfield | billdimensionfield多语言文本 | varchar | 255 |  | √ | ' ' | billdimensionfield多语言文本 |
| 3 | fbilldimensionfieldsmp | 单据短编码 | varchar | 255 |  | √ | ' ' | 单据短编码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbilldimensionfieldkey | 单据字段KEY | varchar | 255 |  | √ | ' ' | 单据字段KEY |
| 6 | fbilldimensionform | 维度FormID | varchar | 50 |  | √ | ' ' | 维度FormID |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fbilldimensionfield | 单据字段 | varchar | 255 |  | √ | ' ' | 单据字段 |
| 10 | fiscontainself | 包含自身 | bpchar | 1 |  | √ | '0' | 包含自身 |
| 11 | fbilldimension | 维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpm_ctrlbilldim |  | fdetailid |
| 2 | idx_fpm_ctrlbilldim_fk |  | fentryid |

---

## 控制数据子单据体-多语言表 t_fpm_ctrlbilldata_l

- **表名称：** 控制数据子单据体-多语言表
- **表名：** t_fpm_ctrlbilldata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmbillwritebackfield | billwritebackfield多语言文本 | varchar | 255 |  | √ | ' ' | billwritebackfield多语言文本 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fmbilldatafield | billdatafield多语言文本 | varchar | 255 |  | √ | ' ' | billdatafield多语言文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_ctrlbilldata_l |  | fdetailid,flocaleid |
| 2 | pk_fpm_ctrlbilldata_l |  | fpkid |

---

## 控制单据单据体-多语言表 t_fpm_ctrlbill_l

- **表名称：** 控制单据单据体-多语言表
- **表名：** t_fpm_ctrlbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmbillcurrency | billcurrency多语言文本 | varchar | 255 |  | √ | ' ' | billcurrency多语言文本 |
| 2 | fmbilldept | billdept多语言文本 | varchar | 255 |  | √ | ' ' | billdept多语言文本 |
| 3 | fmbilldate | billdate多语言文本 | varchar | 255 |  | √ | ' ' | billdate多语言文本 |
| 4 | fmremarkfield | remarkfield多语言文本 | varchar | 2000 |  | √ | ' ' | remarkfield多语言文本 |
| 5 | fmeffectname | effectname多语言文本 | varchar | 255 |  | √ | ' ' | effectname多语言文本 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fmbillorg | billorg多语言文本 | varchar | 255 |  | √ | ' ' | billorg多语言文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_ctrlbill_l |  | fentryid,flocaleid |
| 2 | pk_fpm_ctrlbill_l |  | fpkid |

---

## 控制项目数据类型单据体-子表 t_fpm_ctrldata

- **表名称：** 控制项目数据类型单据体-子表
- **表名：** t_fpm_ctrldata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbusinesstype | 预算业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_ctrldata_fk |  | fid |
| 2 | pk_fpm_ctrldata |  | fentryid |
