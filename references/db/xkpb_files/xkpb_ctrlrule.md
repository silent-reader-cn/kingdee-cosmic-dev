# 项目预算控制规则-xkpb_ctrlrule

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
| 16 | fbilldatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |

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

## 控制项目数据类型单据体-子表 t_xkbm_ctrldata

- **表名称：** 控制项目数据类型单据体-子表
- **表名：** t_xkbm_ctrldata

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
| 1 | idx_xkbm_ctrldata_fk |  | fid |
| 2 | pk_xkbm_ctrldata |  | fentryid |
| 3 | idx_xkbm_ctrldata_type |  | fitemdatatype |

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

## 项目预算控制规则-主表 t_xkbm_ctrlrule

- **表名称：** 项目预算控制规则-主表
- **表名：** t_xkbm_ctrlrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [项目预算控制规则分组 xkpb_ctrlrulegroup](../xkpb_files/xkpb_ctrlrulegroup.md) |
| 3 | fctrlruleeffect | 生效条件 | varchar | 2000 |  | √ | ' ' | 生效条件 |
| 4 | fctrlcycle | 控制周期 | bpchar | 1 |  | √ | ' ' | 控制周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fbyperiod | 按 | bpchar | 1 |  | √ | ' ' | 按,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 7 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | ' ' | 是否系统预置 |
| 8 | fiscycletotal | 按大周期汇总控制 | bpchar | 1 |  | √ | ' ' | 按大周期汇总控制 |
| 9 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fctrlpolicy | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: 2 :实际数小于等于预算数 4 :实际数小于预算数 1 :实际数大于等于预算数 3 :实际数大于预算数 |
| 11 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 12 | fpasswhennull | 预算数为空时通过 | bpchar | 1 |  | √ | ' ' | 预算数为空时通过 |
| 13 | fuseto | 用途 | varchar | 10 |  | √ | '0' | 用途,枚举: 0 :控制与分析 1 :仅分析 |
| 14 | fctrlorgsum | 汇总 | bpchar | 1 |  | √ | '0' | 汇总 |
| 15 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 16 | fisperiodcumctrl | 年内按期累计控制 | bpchar | 1 |  | √ | ' ' | 年内按期累计控制 |
| 17 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 18 | fwizardscheme | 预算数来源 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 19 | fbgcurrency | 预算本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | factsource | 实际数来源 | bpchar | 1 |  | √ | ' ' | 实际数来源,枚举: 1 :仅单据 2 :单据及实际数报表 3 :仅实际数报表 |
| 21 | fprevailrightruledims | fprevailrightruledims | bpchar | 1 |  | √ | '0' |  |
| 22 | fisyearcumctrl | 跨年按期累计控制 | bpchar | 1 |  | √ | ' ' | 跨年按期累计控制 |
| 23 | fisyearsumctrl | 跨年汇总控制 | bpchar | 1 |  | √ | ' ' | 跨年汇总控制 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fwarptype | 偏差方式 | bpchar | 1 |  | √ | ' ' | 偏差方式,枚举: 1 :偏差率（%） 2 :偏差额 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fcounttype | 统计方式 | bpchar | 1 |  | √ | ' ' | 统计方式,枚举: 1 :汇总 2 :以实际数报表为准 |
| 29 | fcalcpolicy | 计算方式 | bpchar | 1 |  | √ | ' ' | 计算方式,枚举: 1 :首记录 2 :最大值 3 :最小值 4 :平均值 5 :末记录 6 :汇总值 |
| 30 | fruletype | 控制规则类型 | varchar | 10 |  | √ | '0' | 控制规则类型,枚举: 0 :普通 1 :动态 2 :项目 |
| 31 | fiscalcbillback | 申请占用释放（下游单据反写字段） | bpchar | 1 |  | √ | ' ' | 申请占用释放（下游单据反写字段） |
| 32 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 35 | fwarptypeprice | 偏差方式 | bpchar | 1 |  | √ | ' ' | 偏差方式,枚举: 1 :偏差率（%） 2 :偏差额 |
| 36 | fvirtuallywriteback | 虚拟反写 | bpchar | 1 |  | √ | '0' | 虚拟反写 |
| 37 | fctrlruleeffectsql | 生效条件sql | varchar | 2000 |  | √ | ' ' | 生效条件sql |
| 38 | fiscalcbill | 单据字段 | bpchar | 1 |  | √ | ' ' | 单据字段 |
| 39 | fxkbmbusinessservice | 所属应用 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fcurrency | 币种 | varchar | 50 |  | √ | ' ' | 币种,枚举: |
| 43 | fpasswhennomapping | 费用项目无成本子要素对应关系通过 | bpchar | 1 |  | √ | '1' | 费用项目无成本子要素对应关系通过 |
| 44 | fcontroltype | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: 2 :实际数小于等于预算数 4 :实际数小于预算数 1 :实际数大于等于预算数 3 :实际数大于预算数 |
| 45 | fexectitle | 预算执行进度提示百分比 | numeric | 23 | 10 | √ | 0 | 预算执行进度提示百分比 |
| 46 | fwarpvalueprice | 偏差值 | numeric | 23 | 10 | √ | 0 | 偏差值 |
| 47 | fctrlruleeffectjson | 生效条件JSON | varchar | 2000 |  | √ | ' ' | 生效条件JSON |
| 48 | frightrateformula | frightrateformula | varchar | 1000 |  | √ | ' ' |  |
| 49 | fshowbggroup | 预算执行按钮组 | varchar | 30 |  | √ | '1' | 预算执行按钮组,枚举: 1 :始终提示 2 :执行到 |
| 50 | fpasswhenmappingnull | 映射关系不存在时通过 | bpchar | 1 |  | √ | ' ' | 映射关系不存在时通过 |
| 51 | fwarpvalue | 偏差值 | numeric | 23 | 10 | √ | 0 | 偏差值 |
| 52 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 53 | fleftrateformula | fleftrateformula | varchar | 1000 |  | √ | ' ' |  |
| 54 | fisshow | 未超预算提示 | bpchar | 1 |  | √ | ' ' | 未超预算提示 |

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

## 控制维度单据体-子表 t_xkbm_ctrldim

- **表名称：** 控制维度单据体-子表
- **表名：** t_xkbm_ctrldim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattributefieldsmp | 属性字段短编码 | varchar | 255 |  | √ | ' ' | 属性字段短编码 |
| 3 | fdimcustgroup | 分组汇总方案 | int8 | 64 |  | √ | 0 | [维度自定义分组 xkbm_dimcustgroup](../xkbm_files/xkbm_dimcustgroup.md) |
| 4 | fdimeffectname | 维度过滤 | varchar | 2000 |  | √ | ' ' | 维度过滤 |
| 5 | fattributefield | 属性字段 | varchar | 255 |  | √ | ' ' | 属性字段 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fattributefieldkey | 属性字段KEY | varchar | 255 |  | √ | ' ' | 属性字段KEY |
| 8 | fctrldimmap | 维度映射 | int8 | 64 |  | √ | 0 | [预算维度映射 xkbm_dimmapping](../xkbm_files/xkbm_dimmapping.md) |
| 9 | fdimeffectkey | 维度过滤条件 | varchar | 2000 |  | √ | ' ' | 维度过滤条件 |
| 10 | ffiltername | 维度范围 | varchar | 2000 |  | √ | ' ' | 维度范围 |
| 11 | fdimensionformid | 维度业务对象ID | varchar | 50 |  | √ | ' ' | 维度业务对象ID |
| 12 | fassistantgroupid | 辅助资料分组 | varchar | 50 |  | √ | ' ' | 辅助资料分组 |
| 13 | fdimeffectdesc | 过滤条件JSON | varchar | 2000 |  | √ | ' ' | 过滤条件JSON |
| 14 | fisdimensionsum | 汇总 | bpchar | 1 |  | √ | ' ' | 汇总 |
| 15 | fdimeffect | dimeffect多语言文本 | varchar | 2000 |  | √ | ' ' | dimeffect多语言文本 |
| 16 | fdimensionsumtype | 汇总类型 | bpchar | 1 |  | √ | ' ' | 汇总类型,枚举: 0 :按明细汇总 1 :按属性汇总 2 :按分组汇总 |
| 17 | fmattributefield | attributefield多语言文本 | varchar | 255 |  | √ | ' ' | attributefield多语言文本 |
| 18 | ffilterkey | 维度范围Sql | varchar | 2000 |  | √ | ' ' | 维度范围Sql |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fdimension | 维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 21 | fattributeformid | 属性业务对象ID | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

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
| 10 | fprebillform | 上游受控单据（弃用） | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fbillorgsmp | 业务组织来源短字段 | varchar | 50 |  | √ | ' ' | 业务组织来源短字段 |
| 12 | fallsinglefilter | 生效条件字段名称 | varchar | 255 |  | √ | ' ' | 生效条件字段名称 |
| 13 | fcurbillformnum | 当前单据分录编码 | int8 | 64 |  | √ | 0 | 当前单据分录编码 |
| 14 | fbillcurrency | 单据币种 | varchar | 255 |  | √ | ' ' | 单据币种 |
| 15 | fbilldeptkey | 部门来源字段 | varchar | 100 |  | √ | ' ' | 部门来源字段 |
| 16 | fremarkfieldkey | 备注信息字段 | varchar | 2000 |  | √ | ' ' | 备注信息字段 |
| 17 | fmremarkfield | remarkfield多语言文本 | varchar | 2000 |  | √ | ' ' | remarkfield多语言文本 |
| 18 | fmeffectname | effectname多语言文本 | varchar | 255 |  | √ | ' ' | effectname多语言文本 |
| 19 | fbillcurrencysmp | 币种短字段 | varchar | 50 |  | √ | ' ' | 币种短字段 |
| 20 | fbilldeptsmp | 部门来源短字段 | varchar | 50 |  | √ | ' ' | 部门来源短字段 |
| 21 | fremarkfieldsmp | 备注信息短字段 | varchar | 2000 |  | √ | ' ' | 备注信息短字段 |
| 22 | fbilldept | 部门来源 | varchar | 255 |  | √ | ' ' | 部门来源 |
| 23 | fbillform | 控制单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fbillcurrencykey | 币种字段 | varchar | 100 |  | √ | ' ' | 币种字段 |
| 25 | fbillorgkey | 业务组织来源字段 | varchar | 100 |  | √ | ' ' | 业务组织来源字段 |
| 26 | fmbilldept | billdept多语言文本 | varchar | 255 |  | √ | ' ' | billdept多语言文本 |
| 27 | fbillproperty | 引用属性 | int4 | 32 |  | √ | 0 | 引用属性 |
| 28 | ffilterrows | 生效条件JSON | varchar | 2000 |  | √ | ' ' | 生效条件JSON |
| 29 | fremarkfield | 备注信息 | varchar | 2000 |  | √ | ' ' | 备注信息 |
| 30 | feffectkey | 生效条件Sql | varchar | 2000 |  | √ | ' ' | 生效条件Sql |
| 31 | feffectname | 生效条件 | varchar | 255 |  | √ | ' ' | 生效条件 |
| 32 | fprebillformnum | 上游受控单据 | varchar | 50 |  | √ | ' ' | 上游受控单据,枚举: |
| 33 | fwritebacktiming | 反写时机 | varchar | 50 |  | √ | ' ' | 反写时机,枚举: save :保存 submit :提交 |
| 34 | fbillorg | 组织来源 | varchar | 255 |  | √ | ' ' | 组织来源 |
| 35 | fbilldatekey | 单据日期字段 | varchar | 100 |  | √ | ' ' | 单据日期字段 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | fratetype | 汇率类型 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 38 | fallsinglefilter_tag | 生效条件字段名称_详情 | text | 0 |  |  | null | 生效条件字段名称_详情 |

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

## 项目预算控制规则-多语言表 t_xkbm_ctrlrule_l

- **表名称：** 项目预算控制规则-多语言表
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

## 生效组织-多选基础资料表 t_xkbm_effectorgunit

- **表名称：** 生效组织-多选基础资料表
- **表名：** t_xkbm_effectorgunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
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

## 映射维度-多选基础资料表 t_xkbm_mappingctrldim

- **表名称：** 映射维度-多选基础资料表
- **表名：** t_xkbm_mappingctrldim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_mappingctrldim |  | fpkid |
| 2 | idx_xkbm_mappingctrldim |  | fentryid |

---

## 维度映射-多选基础资料表 t_xkbm_ruledimmapping

- **表名称：** 维度映射-多选基础资料表
- **表名：** t_xkbm_ruledimmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [预算维度映射 xkbm_dimmapping](../xkbm_files/xkbm_dimmapping.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ruledimmapping |  | fpkid |
| 2 | idx_xkbm_ruledimmapping |  | fid |

---

## 受控组织-多选基础资料表 t_xkpb_ctrlruleorg

- **表名称：** 受控组织-多选基础资料表
- **表名：** t_xkpb_ctrlruleorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkpb_ctrlruleorg |  | fpkid |
| 2 | idx_xkpb_ctrlruleorg_fid |  | fid |

---

## 控制维度子单据体-子表 t_xkbm_ctrlbilldim

- **表名称：** 控制维度子单据体-子表
- **表名：** t_xkbm_ctrlbilldim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmbilldimensionfield | billdimensionfield多语言文本 | varchar | 255 |  | √ | ' ' | billdimensionfield多语言文本 |
| 2 | foriginbilldimension | 映射前维度 | varchar | 255 |  | √ | ' ' | 映射前维度 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcontainalllevel | 包含所有下级 | bpchar | 1 |  | √ | '0' | 包含所有下级 |
| 5 | fbilldimmap | 维度映射 | int8 | 64 |  | √ | 0 | [预算维度映射 xkbm_dimmapping](../xkbm_files/xkbm_dimmapping.md) |
| 6 | fbilldimension | 维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 7 | fbilldimensionfieldsmp | 单据短编码 | varchar | 255 |  | √ | ' ' | 单据短编码 |
| 8 | fbilldimensionfieldkey | 单据字段KEY | varchar | 255 |  | √ | ' ' | 单据字段KEY |
| 9 | fbilldimensionform | 维度FormID | varchar | 50 |  | √ | ' ' | 维度FormID |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fbilldimensionfield | 单据字段 | varchar | 255 |  | √ | ' ' | 单据字段 |
| 13 | fiscontainself | 包含自身 | bpchar | 1 |  | √ | ' ' | 包含自身 |

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
