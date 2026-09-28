# 结转损益-gl_transplprogram

## 结转损益-主表 t_gl_transplprogram

- **表名称：** 结转损益-主表
- **表名：** t_gl_transplprogram

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fismultiplebook | 是否多账簿 | varchar | 10 |  | √ | ' ' | 是否多账簿 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fchkbyasstaccount | fchkbyasstaccount | bpchar | 1 |  | √ | '0' |  |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fisdesacct | 指定科目结转 | bpchar | 1 |  | √ | '0' | 指定科目结转 |
| 8 | fchkyearprofitbyoriginal | 本年利润按本位币结转 | bpchar | 1 |  | √ | '0' | 本年利润按本位币结转 |
| 9 | fcurperiod | fcurperiod | int8 | 64 |  | √ | 0 |  |
| 10 | fdptname | fdptname | varchar | 30 |  | √ | ' ' |  |
| 11 | fchkbypl | 收益和损失分别生成 | bpchar | 1 |  | √ | '0' | 收益和损失分别生成 |
| 12 | faccountbook | faccountbook | int8 | 64 |  | √ | 0 |  |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 15 | fchkbybalancereverse | fchkbybalancereverse | bpchar | 1 |  | √ | '0' |  |
| 16 | fincurredamount | fincurredamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: 0 :禁用 1 :启用 |
| 18 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fvoucherdesc | 凭证摘要 | varchar | 255 |  | √ | ' ' | 凭证摘要 |
| 21 | fdptnames | fdptnames | int8 | 64 |  | √ | 0 |  |
| 22 | fvouchernumber | fvouchernumber | varchar | 1000 |  | √ | ' ' |  |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fbookid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 25 | fvouchertypeid | 凭证字 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 26 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 27 | fradiogroup_acc | fradiogroup_acc | bpchar | 1 |  | √ | '0' |  |
| 28 | fradiogroup_ass | fradiogroup_ass | bpchar | 1 |  | √ | '0' |  |
| 29 | funposthandle | 未过账凭证处理方式 | bpchar | 1 |  | √ | '0' | 未过账凭证处理方式,枚举: 0 :终止处理 1 :忽略未过账凭证 2 :包含已提交未过账凭证 |
| 30 | fyearprofitacct | 本年利润科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 31 | fvoucherdatetype | fvoucherdatetype | bpchar | 1 |  | √ | '0' |  |
| 32 | fgeneratedamount | fgeneratedamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 33 | fperiod | fperiod | bpchar | 1 |  | √ | '0' |  |
| 34 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 35 | fistransplbybalance | 按余额反方向结转 | bpchar | 1 |  | √ | '0' | 按余额反方向结转 |
| 36 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_transpl_forgid_bookid |  | forgid,fbookid |
| 2 | t_gl_transplprogram_pkey |  | fid |

---

## 结转损益-多语言表 t_gl_transplprogram_l

- **表名称：** 结转损益-多语言表
- **表名：** t_gl_transplprogram_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fvoucherdesc | 凭证摘要 | varchar | 255 |  | √ | ' ' | 凭证摘要 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_transplprogram_l |  | fid,flocaleid |
| 2 | t_gl_transplprogram_l_pkey |  | fpkid |

---

## 结转科目-多选基础资料表 t_gl_transpl_account

- **表名称：** 结转科目-多选基础资料表
- **表名：** t_gl_transpl_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_transpl_account_pkey |  | fpkid |
| 2 | idx_gl_transpl_account |  | fid |
