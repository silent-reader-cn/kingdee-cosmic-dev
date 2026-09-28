# 期末调汇-gl_adjustexchangerate

## 期末调汇-主表 t_gl_adjustexchangerate

- **表名称：** 期末调汇-主表
- **表名：** t_gl_adjustexchangerate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flossassgrpid | 损失科目核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbybalancereverse | 按余额相反方向调汇 | bpchar | 1 |  | √ | '0' | 按余额相反方向调汇 |
| 5 | fismultiplebook | 是否多账簿 | bpchar | 1 |  | √ | '0' | 是否多账簿 |
| 6 | fplaccountid | 汇兑损益科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率差 | varchar | 30 |  | √ | ' ' | 汇率差 |
| 9 | fratemonthbtngrp | 指定月份按钮组 | bpchar | 1 |  | √ | '1' | 指定月份按钮组,枚举: 1 :当期 2 :下期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fadjuststyle | 调汇方式 | bpchar | 1 |  | √ | '1' | 调汇方式,枚举: 1 :按实时汇率 2 :按指定汇率 3 :按指定日期汇率 |
| 12 | fpldirectionctrl | 固定汇兑损益科目生成方向 | varchar | 2 |  | √ | '0' | 固定汇兑损益科目生成方向,枚举: 0 :不控制 1 :借 -1 :贷 |
| 13 | fdate | 日期 | bpchar | 1 |  | √ | '1' | 日期,枚举: 1 :期初第一天 2 :期末最后一天 |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 15 | fnonegative | 余额为负不调汇 | bpchar | 1 |  | √ | '0' | 余额为负不调汇 |
| 16 | flossaccountid | 汇兑损失科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 21 | fvoucherdesc | 凭证摘要 | varchar | 255 |  | √ | ' ' | 凭证摘要 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fadjustpricekind | fadjustpricekind | bpchar | 1 |  | √ | '1' |  |
| 24 | fvouchernumber | fvouchernumber | varchar | 30 |  | √ | ' ' |  |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fbookstypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 27 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 28 | fvouchertypeid | 凭证字 | int8 | 64 |  | √ | 0 | [凭证字 gl_vouchertype](../gl_files/gl_vouchertype.md) |
| 29 | fissetcuruency | 币种调汇类别 | bpchar | 1 |  | √ | '0' | 币种调汇类别,枚举: 1 :全部币种 2 :指定币种 |
| 30 | fbypl | 按照收益、损失分开调汇 | bpchar | 1 |  | √ | '0' | 按照收益、损失分开调汇 |
| 31 | fvoucherdatetype | 凭证日期 | bpchar | 1 |  | √ | '0' | 凭证日期,枚举: 1 :期末最后一天 2 :系统日期 |
| 32 | faccounttype | 科目类型 | bpchar | 1 |  | √ | '1' | 科目类型,枚举: 1 :财务会计 2 :预算会计 |
| 33 | fuselistprice | fuselistprice | bpchar | 1 |  | √ | '1' |  |
| 34 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 35 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 36 | fissetaccount | 科目调汇类别 | bpchar | 1 |  | √ | '0' | 科目调汇类别,枚举: 1 :全部科目 2 :指定科目 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_adjustexchangerate |  | forgid,fbookid |
| 2 | t_gl_adjustexchangerate_pkey |  | fid |

---

## 调汇核算维度-子表 t_gl_adjust_assgrp

- **表名称：** 调汇核算维度-子表
- **表名：** t_gl_adjust_assgrp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftxtval | 手工纬度值 | varchar | 2000 |  | √ | ' ' | 手工纬度值 |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | ffieldnameid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_adjust_assgrp_pkey |  | fdetailid |
| 2 | idx_gl_adjust_assgrp |  | fentryid |

---

## 报告币汇率-子表 t_gl_adjexchangerate_rpt

- **表名称：** 报告币汇率-子表
- **表名：** t_gl_adjexchangerate_rpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_adjexchangerate_rpt |  | fid |
| 2 | t_gl_adjexchangerate_rpt_pkey |  | fentryid |

---

## 期末调汇-多语言表 t_gl_adjustexchangerate_l

- **表名称：** 期末调汇-多语言表
- **表名：** t_gl_adjustexchangerate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_adjustexchangerate_l_pkey |  | fpkid |
| 2 | idx_gl_adjustexchangerate_l |  | fid,flocaleid |

---

## 科目调汇-子表 t_gl_adjexchangerate_acc

- **表名称：** 科目调汇-子表
- **表名：** t_gl_adjexchangerate_acc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassgrpdesc | 核算维度 | varchar | 50 |  | √ | ' ' | 核算维度 |
| 3 | fisrptexchange | fisrptexchange | bpchar | 1 |  | √ | '0' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fiscurexchange | 本位币调汇 | bpchar | 1 |  | √ | '0' | 本位币调汇 |
| 7 | faccountid | 科目编码 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_adjexchangerate_acc |  | fid |
| 2 | t_gl_adjexchangerate_acc_pkey |  | fentryid |

---

## 维度值-多选基础资料表 t_gl_adjust_assmulval

- **表名称：** 维度值-多选基础资料表
- **表名：** t_gl_adjust_assmulval

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [科目影响因素（旧） ai_vchentrytype](../ai_files/ai_vchentrytype.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_adjust_assmulval_pkey |  | fpkid |
| 2 | idx_gl_adjust_assmulval |  | fdetailid |

---

## 本位币汇率-子表 t_gl_adjexchangerate_loc

- **表名称：** 本位币汇率-子表
- **表名：** t_gl_adjexchangerate_loc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_adjexchangerate_loc |  | fid |
| 2 | t_gl_adjexchangerate_loc_pkey |  | fentryid |
