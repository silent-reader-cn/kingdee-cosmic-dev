# 比率预算控制规则-xkbm_ratectrlrule

## 控制项目数据类型单据体-子表 t_xkbm_ctrldata

- **表名称：** 控制项目数据类型单据体-子表
- **表名：** t_xkbm_ctrldata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbusinesstype | 预算业务类型 | int8 | 64 |  | √ | 0 | 预算业务类型 xkbm_businesstype |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbm_rptitemdatatype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_ctrldata_fk |  | fid |
| 2 | pk_xkbm_ctrldata |  | fentryid |
| 3 | idx_xkbm_ctrldata_type |  | fitemdatatype |

---

## 计算公式中的项目数据类型-多选基础资料表 t_xkbm_formulaitemdata

- **表名称：** 计算公式中的项目数据类型-多选基础资料表
- **表名：** t_xkbm_formulaitemdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目数据类型 xkbm_rptitemdatatype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_formulaitemdata |  | fpkid |
| 2 | idx_xkbm_formulaitemdata |  | fid |

---

## 控制维度子单据体-多语言表 t_xkbm_ctrlbilldim_l

- **表名称：** 控制维度子单据体-多语言表
- **表名：** t_xkbm_ctrlbilldim_l

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
| 1 | pk_xkbm_ctrlbilldim_l |  | fpkid |
| 2 | idx_xkbm_ctrlbdim_l |  | fdetailid,flocaleid |

---

## 控制数据子单据体-子表 t_xkbm_ctrlbilldata

- **表名称：** 控制数据子单据体-子表
- **表名：** t_xkbm_ctrlbilldata

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
| 12 | fbillwritebackfield | 申请占用释放（下游单据反写字段） | varchar | 255 |  | √ | ' ' | 申请占用释放（下游单据反写字段） |
| 13 | fbillwritebackfieldsmp | 申请占用释放短字段 | varchar | 50 |  | √ | ' ' | 申请占用释放短字段 |
| 14 | fprebillfieldsmp | 反写上游单据短字段 | varchar | 50 |  | √ | ' ' | 反写上游单据短字段 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | fbilldatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbm_rptitemdatatype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrlbilldata |  | fdetailid |
| 2 | idx_xkbm_ctrlbilldata_fk |  | fentryid |
| 3 | idx_xkbm_ctrlbilldata_type |  | fbilldatatype |

---

## 控制操作与强度子单据体-子表 t_xkbm_rateopratectrl

- **表名称：** 控制操作与强度子单据体-子表
- **表名：** t_xkbm_rateopratectrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fratectrllevel | 控制强度 | varchar | 50 |  | √ | ' ' | 控制强度,枚举: 1 :不控制 2 :提示 3 :强制 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fratectrloprate | 控制操作 | varchar | 50 |  | √ | ' ' | 控制操作,枚举: submit :提交 audit :审核 unsubmit :撤销 unaudit :反审核 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rateopratectrl |  | fentryid |
| 2 | pk_xkbm_rateopratectrl |  | fdetailid |

---

## 比率预算控制规则-主表 t_xkbm_ctrlrule

- **表名称：** 比率预算控制规则-主表
- **表名：** t_xkbm_ctrlrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 比率预算控制规则分组 xkbm_ratectrlrulegroup |
| 3 | fctrlruleeffect | 生效条件 | varchar | 2000 |  | √ | ' ' | 生效条件 |
| 4 | fctrlcycle | 控制周期 | bpchar | 1 |  | √ | ' ' | 控制周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fbyperiod | 按 | bpchar | 1 |  | √ | ' ' | 按,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 7 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | ' ' | 是否系统预置 |
| 8 | fiscycletotal | 按大周期汇总控制 | bpchar | 1 |  | √ | ' ' | 按大周期汇总控制 |
| 9 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fctrlpolicy | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: 2 :实际数小于等于预算数 4 :实际数小于预算数 1 :实际数大于等于预算数 3 :实际数大于预算数 |
| 11 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 12 | fpasswhennull | 预算数为空时通过 | bpchar | 1 |  | √ | ' ' | 预算数为空时通过 |
| 13 | fuseto | fuseto | varchar | 10 |  | √ | '0' |  |
| 14 | fctrlorgsum | 汇总 | bpchar | 1 |  | √ | '0' | 汇总 |
| 15 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 16 | fisperiodcumctrl | 年内按期累计控制 | bpchar | 1 |  | √ | ' ' | 年内按期累计控制 |
| 17 | fwizardscheme | 预算数来源 | int8 | 64 |  | √ | 0 | 预算模板样式方案 xkbm_rptscheme |
| 18 | fbgcurrency | 预算本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | factsource | 实际数来源 | bpchar | 1 |  | √ | ' ' | 实际数来源,枚举: 1 :仅单据 2 :单据及实际数报表 3 :仅实际数报表 |
| 20 | fisyearcumctrl | 跨年按期累计控制 | bpchar | 1 |  | √ | ' ' | 跨年按期累计控制 |
| 21 | fisyearsumctrl | 跨年汇总控制 | bpchar | 1 |  | √ | ' ' | 跨年汇总控制 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fwarptype | 偏差方式 | bpchar | 1 |  | √ | ' ' | 偏差方式,枚举: 1 :偏差率（%） 2 :偏差额 |
| 25 | fcounttype | 统计方式 | bpchar | 1 |  | √ | ' ' | 统计方式,枚举: 1 :汇总 2 :以实际数报表为准 |
| 26 | fcalcpolicy | 计算方式 | bpchar | 1 |  | √ | ' ' | 计算方式,枚举: 1 :首记录 2 :最大值 3 :最小值 4 :平均值 5 :末记录 |
| 27 | fruletype | 控制规则类型 | varchar | 10 |  | √ | '0' | 控制规则类型,枚举: 0 :普通 1 :动态 |
| 28 | fiscalcbillback | 申请占用释放（下游单据反写字段） | bpchar | 1 |  | √ | ' ' | 申请占用释放（下游单据反写字段） |
| 29 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 32 | fwarptypeprice | 偏差方式 | bpchar | 1 |  | √ | ' ' | 偏差方式,枚举: 1 :偏差率（%） 2 :偏差额 |
| 33 | fvirtuallywriteback | 虚拟反写 | bpchar | 1 |  | √ | '0' | 虚拟反写 |
| 34 | fctrlruleeffectsql | 生效条件sql | varchar | 2000 |  | √ | ' ' | 生效条件sql |
| 35 | fiscalcbill | 单据字段 | bpchar | 1 |  | √ | ' ' | 单据字段 |
| 36 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | 预算业务服务 xkbm_businessservice |
| 37 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 39 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别,枚举: |
| 40 | fpasswhennomapping | 费用项目无成本子要素对应关系通过 | bpchar | 1 |  | √ | '1' | 费用项目无成本子要素对应关系通过 |
| 41 | fcontroltype | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: 2 :实际数小于等于预算数 4 :实际数小于预算数 1 :实际数大于等于预算数 3 :实际数大于预算数 |
| 42 | fexectitle | 预算执行进度提示百分比 | numeric | 23 | 10 | √ | 0 | 预算执行进度提示百分比 |
| 43 | fwarpvalueprice | 偏差值 | numeric | 23 | 10 | √ | 0 | 偏差值 |
| 44 | fctrlruleeffectjson | 生效条件JSON | varchar | 2000 |  | √ | ' ' | 生效条件JSON |
| 45 | frightrateformula | 分母 | varchar | 1000 |  | √ | ' ' | 分母 |
| 46 | fshowbggroup | 预算执行按钮组 | varchar | 30 |  | √ | '1' | 预算执行按钮组,枚举: 1 :始终提示 2 :执行到 |
| 47 | fwarpvalue | 偏差值 | numeric | 23 | 10 | √ | 0 | 偏差值 |
| 48 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 49 | fleftrateformula | 分子 | varchar | 1000 |  | √ | ' ' | 分子 |
| 50 | fisshow | 未超预算提示 | bpchar | 1 |  | √ | ' ' | 未超预算提示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrlrule |  | fid |
| 2 | idx_xkbm_ctrlrule_num |  | fnumber |

---

## 计算公式中的业务类型-多选基础资料表 t_xkbm_formulabiztype

- **表名称：** 计算公式中的业务类型-多选基础资料表
- **表名：** t_xkbm_formulabiztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 预算业务类型 xkbm_businesstype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_formulabiztype |  | fpkid |
| 2 | idx_xkbm_formulabiztype |  | fid |

---

## 控制维度单据体-子表 t_xkbm_ctrldim

- **表名称：** 控制维度单据体-子表
- **表名：** t_xkbm_ctrldim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattributefieldsmp | 属性字段短编码 | varchar | 255 |  | √ | ' ' | 属性字段短编码 |
| 3 | fdimeffectname | 维度过滤 | varchar | 2000 |  | √ | ' ' | 维度过滤 |
| 4 | fattributefield | 属性字段 | varchar | 255 |  | √ | ' ' | 属性字段 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fattributefieldkey | 属性字段KEY | varchar | 255 |  | √ | ' ' | 属性字段KEY |
| 7 | fdimeffectkey | 维度过滤条件 | varchar | 2000 |  | √ | ' ' | 维度过滤条件 |
| 8 | ffiltername | 维度范围 | varchar | 2000 |  | √ | ' ' | 维度范围 |
| 9 | fdimensionformid | 维度业务对象ID | varchar | 50 |  | √ | ' ' | 维度业务对象ID |
| 10 | fassistantgroupid | 辅助资料分组 | varchar | 50 |  | √ | ' ' | 辅助资料分组 |
| 11 | fdimeffectdesc | 过滤条件JSON | varchar | 2000 |  | √ | ' ' | 过滤条件JSON |
| 12 | fisdimensionsum | 汇总 | bpchar | 1 |  | √ | ' ' | 汇总 |
| 13 | fdimeffect | dimeffect多语言文本 | varchar | 2000 |  | √ | ' ' | dimeffect多语言文本 |
| 14 | fdimensionsumtype | 汇总类型 | bpchar | 1 |  | √ | ' ' | 汇总类型,枚举: 0 :按明细汇总 1 :按属性汇总 2 :自定义分组汇总 |
| 15 | fmattributefield | attributefield多语言文本 | varchar | 255 |  | √ | ' ' | attributefield多语言文本 |
| 16 | ffilterkey | 维度范围Sql | varchar | 2000 |  | √ | ' ' | 维度范围Sql |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fdimension | 维度 | int8 | 64 |  | √ | 0 | 维度 xkrpt_dimension |
| 19 | fattributeformid | 属性业务对象ID | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_ctrldim_fk |  | fid |
| 2 | idx_xkbm_ctrldim_dim |  | fdimension |
| 3 | pk_xkbm_ctrldim |  | fentryid |

---

## 控制维度单据体-多语言表 t_xkbm_ctrldim_l

- **表名称：** 控制维度单据体-多语言表
- **表名：** t_xkbm_ctrldim_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdimeffect | dimeffect多语言文本 | varchar | 2000 |  | √ | ' ' | dimeffect多语言文本 |
| 2 | fmattributefield | attributefield多语言文本 | varchar | 255 |  | √ | ' ' | attributefield多语言文本 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrldim_l |  | fpkid |
| 2 | idx_xkbm_ctrldim_l |  | fentryid,flocaleid |

---

## 控制操作与强度单据体-子表 t_xkbm_opratectrl

- **表名称：** 控制操作与强度单据体-子表
- **表名：** t_xkbm_opratectrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fctrllevel | 控制强度 | bpchar | 1 |  | √ | ' ' | 控制强度,枚举: 1 :不控制 2 :提示 3 :强制 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fctrloprate | 控制操作 | varchar | 50 |  | √ | ' ' | 控制操作,枚举: submit :提交 audit :审核 unsubmit :撤销 unaudit :反审核 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_opratectrl_fk |  | fentryid |
| 2 | idx_xkbm_opratectrl_op |  | fctrloprate |
| 3 | pk_xkbm_opratectrl |  | fdetailid |

---

## 计算公式中的预算控制规则-多选基础资料表 t_xkbm_formulactrlrule

- **表名称：** 计算公式中的预算控制规则-多选基础资料表
- **表名：** t_xkbm_formulactrlrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 预算控制规则 xkbm_ctrlrule |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_formulactrlrule |  | fpkid |
| 2 | idx_xkbm_formulactrlrule |  | fid |

---

## 控制单据单据体-多语言表 t_xkbm_ctrlbill_l

- **表名称：** 控制单据单据体-多语言表
- **表名：** t_xkbm_ctrlbill_l

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
| 1 | idx_xkbm_ctrlbill_l |  | fentryid,flocaleid |
| 2 | pk_xkbm_ctrlbill_l |  | fpkid |

---

## 控制单据单据体-子表 t_xkbm_ctrlbill

- **表名称：** 控制单据单据体-子表
- **表名：** t_xkbm_ctrlbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fctrltime | 预算影响类型 | bpchar | 1 |  | √ | ' ' | 预算影响类型,枚举: 1 :申请占用 2 :预算执行 3 :预算冲回 |
| 3 | fbilldatesmp | 单据日期短字段 | varchar | 50 |  | √ | ' ' | 单据日期短字段 |
| 4 | fmbillcurrency | billcurrency多语言文本 | varchar | 255 |  | √ | ' ' | billcurrency多语言文本 |
| 5 | fmbilldate | billdate多语言文本 | varchar | 255 |  | √ | ' ' | billdate多语言文本 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbilldate | 单据日期 | varchar | 255 |  | √ | ' ' | 单据日期 |
| 8 | fmbillorg | billorg多语言文本 | varchar | 255 |  | √ | ' ' | billorg多语言文本 |
| 9 | ftextfield | 单据状态字段 | varchar | 50 |  | √ | ' ' | 单据状态字段 |
| 10 | fprebillform | 上游受控单据（弃用） | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fbillorgsmp | 业务组织来源短字段 | varchar | 50 |  | √ | ' ' | 业务组织来源短字段 |
| 12 | fcurbillformnum | 当前单据分录编码 | int8 | 64 |  | √ | 0 | 当前单据分录编码 |
| 13 | fbillcurrency | 单据币别 | varchar | 255 |  | √ | ' ' | 单据币别 |
| 14 | fbilldeptkey | 部门来源字段 | varchar | 50 |  | √ | ' ' | 部门来源字段 |
| 15 | fremarkfieldkey | 备注信息字段 | varchar | 2000 |  | √ | ' ' | 备注信息字段 |
| 16 | fmremarkfield | remarkfield多语言文本 | varchar | 2000 |  | √ | ' ' | remarkfield多语言文本 |
| 17 | fmeffectname | effectname多语言文本 | varchar | 255 |  | √ | ' ' | effectname多语言文本 |
| 18 | fbillcurrencysmp | 币别短字段 | varchar | 50 |  | √ | ' ' | 币别短字段 |
| 19 | fbilldeptsmp | 部门来源短字段 | varchar | 50 |  | √ | ' ' | 部门来源短字段 |
| 20 | fremarkfieldsmp | 备注信息短字段 | varchar | 2000 |  | √ | ' ' | 备注信息短字段 |
| 21 | fbilldept | 部门来源 | varchar | 255 |  | √ | ' ' | 部门来源 |
| 22 | fbillform | 控制单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 23 | fbillcurrencykey | 币别字段 | varchar | 50 |  | √ | ' ' | 币别字段 |
| 24 | fbillorgkey | 业务组织来源字段 | varchar | 50 |  | √ | ' ' | 业务组织来源字段 |
| 25 | fmbilldept | billdept多语言文本 | varchar | 255 |  | √ | ' ' | billdept多语言文本 |
| 26 | ffilterrows | 生效条件JSON | varchar | 2000 |  | √ | ' ' | 生效条件JSON |
| 27 | fremarkfield | 备注信息 | varchar | 2000 |  | √ | ' ' | 备注信息 |
| 28 | feffectkey | 生效条件Sql | varchar | 2000 |  | √ | ' ' | 生效条件Sql |
| 29 | feffectname | 生效条件 | varchar | 255 |  | √ | ' ' | 生效条件 |
| 30 | fprebillformnum | 上游受控单据 | varchar | 50 |  | √ | ' ' | 上游受控单据,枚举: |
| 31 | fwritebacktiming | 反写时机 | varchar | 50 |  | √ | ' ' | 反写时机,枚举: save :保存 submit :提交 |
| 32 | fbillorg | 组织来源 | varchar | 255 |  | √ | ' ' | 组织来源 |
| 33 | fbilldatekey | 单据日期字段 | varchar | 50 |  | √ | ' ' | 单据日期字段 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fratetype | 汇率类型 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrlbill |  | fentryid |
| 2 | idx_xkbm_ctrlbill_fk |  | fid |
| 3 | idx_xkbm_ctrlbill_form |  | fbillform |

---

## 生效组织-多选基础资料表 t_xkbm_effectorgunit

- **表名称：** 生效组织-多选基础资料表
- **表名：** t_xkbm_effectorgunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 预算组织选择 xkbm_orgselect |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_effectorgunit |  | fid |
| 2 | pk_xkbm_effectorgunit |  | fpkid |

---

## 控制数据子单据体-多语言表 t_xkbm_ctrlbilldata_l

- **表名称：** 控制数据子单据体-多语言表
- **表名：** t_xkbm_ctrlbilldata_l

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
| 1 | idx_xkbm_ctrlbdata_l |  | fdetailid,flocaleid |
| 2 | pk_xkbm_ctrlbilldata_l |  | fpkid |

---

## 比率预算控制规则-多语言表 t_xkbm_ctrlrule_l

- **表名称：** 比率预算控制规则-多语言表
- **表名：** t_xkbm_ctrlrule_l

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
| 1 | idx_xkbm_ctrlrule_l |  | fid,flocaleid |
| 2 | pk_xkbm_ctrlrule_l |  | fpkid |

---

## 控制维度子单据体-子表 t_xkbm_ctrlbilldim

- **表名称：** 控制维度子单据体-子表
- **表名：** t_xkbm_ctrlbilldim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmbilldimensionfield | billdimensionfield多语言文本 | varchar | 255 |  | √ | ' ' | billdimensionfield多语言文本 |
| 2 | fbilldimensionfieldsmp | 单据短编码 | varchar | 255 |  | √ | ' ' | 单据短编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbilldimensionfieldkey | 单据字段KEY | varchar | 255 |  | √ | ' ' | 单据字段KEY |
| 5 | fbilldimensionform | 维度FormID | varchar | 50 |  | √ | ' ' | 维度FormID |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fbilldimensionfield | 单据字段 | varchar | 255 |  | √ | ' ' | 单据字段 |
| 9 | fbilldimension | 维度 | int8 | 64 |  | √ | 0 | 维度 xkrpt_dimension |
| 10 | fiscontainself | 包含自身 | bpchar | 1 |  | √ | ' ' | 包含自身 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_ctrlbilldim_fk |  | fentryid |
| 2 | pk_xkbm_ctrlbilldim |  | fdetailid |
| 3 | idx_xkbm_ctrlbilldim_dim |  | fbilldimension |

---

## 控制单据单据体-子表 t_xkbm_ratectrlbill

- **表名称：** 控制单据单据体-子表
- **表名：** t_xkbm_ratectrlbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fratebillformid | 控制单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | frateeffectname | 生效条件 | varchar | 50 |  | √ | ' ' | 生效条件 |
| 4 | fratebelongentryid | 所属控制单据ID | varchar | 50 |  | √ | ' ' | 所属控制单据ID |
| 5 | fratectrltime | 预算影响类型 | varchar | 10 |  | √ | ' ' | 预算影响类型,枚举: 1 :申请占用 2 :预算执行 3 :预算冲回 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fratebelongctrlruleid | 来源控制规则 | int8 | 64 |  | √ | 0 | 预算控制规则 xkbm_ctrlrule |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ratectrlbill |  | fentryid |
| 2 | idx_xkbm_ratectrlbill_fid |  | fid |
