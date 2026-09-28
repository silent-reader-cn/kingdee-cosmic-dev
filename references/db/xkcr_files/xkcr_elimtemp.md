# 抵销分录模板-xkcr_elimtemp

## 核对维度-多选基础资料表 t_xkcr_elimtemp_dim

- **表名称：** 核对维度-多选基础资料表
- **表名：** t_xkcr_elimtemp_dim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcr_elimtemp_dim |  | fpkid |
| 2 | idx_xkcr_elimtemp_dim_fk |  | fid |

---

## 抵销分录模板-多语言表 t_xkcr_elimtemp_l

- **表名称：** 抵销分录模板-多语言表
- **表名：** t_xkcr_elimtemp_l

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
| 1 | pk_xkcr_elimtemp_l |  | fpkid |
| 2 | idx_xkcr_elimtemp_l |  | fid,flocaleid |

---

## 公司分录-子表 t_xkcr_elimtempcomp

- **表名称：** 公司分录-子表
- **表名：** t_xkcr_elimtempcomp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiseachother | 互为交易方 | bpchar | 1 |  | √ | '0' | 互为交易方 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsell | 销售方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbuy | 购买方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_elimtempcomp |  | fentryid |
| 2 | idx_xkcr_elimcomp_id |  | fid |

---

## 抵销分录-多语言表 t_xkcr_elimtempentry_l

- **表名称：** 抵销分录-多语言表
- **表名：** t_xkcr_elimtempentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fexplanation | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_elimtempentry_l |  | fpkid |
| 2 | idx_xkcr_elimtempentry_l |  | fentryid,flocaleid |

---

## 抵销分录-子表 t_xkcr_elimtempentry

- **表名称：** 抵销分录-子表
- **表名：** t_xkcr_elimtempentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismulesp | 股权分段计算 | bpchar | 1 |  | √ | '0' | 股权分段计算 |
| 3 | felimdirect | 抵销方向 | bpchar | 1 |  | √ | ' ' | 抵销方向,枚举: 0 :未知 1 :正方 2 :反方 |
| 4 | fdc | 借贷方向 | varchar | 2 |  | √ | ' ' | 借贷方向,枚举: 1 :借方 -1 :贷方 2 :条件判断 |
| 5 | fformula | 抵销数 | varchar | 2000 |  | √ | ' ' | 抵销数 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdatasource | 取数来源 | varchar | 3 |  | √ | ' ' | 取数来源,枚举: 17 :个别报表 71 :附表个别报表 31 :抵销表 100 :差额 101 :公式定义 |
| 8 | fdatadirect | 取数方 | bpchar | 1 |  | √ | ' ' | 取数方,枚举: 1 :投资方 2 :被投资方 3 :销售方 4 :购买方 5 :我方 6 :对方 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fexplanation | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |
| 11 | fitemid | 报表项目编码 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 12 | fdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_elimtempentry |  | fentryid |
| 2 | idx_xkcr_elimentrydet_fid |  | fid |

---

## 抵销分录模板-主表 t_xkcr_elimtemp

- **表名称：** 抵销分录模板-主表
- **表名：** t_xkcr_elimtemp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [抵销分录模板类别 xkcr_elimtemptype](../xkcr_files/xkcr_elimtemptype.md) |
| 3 | fusecheckdim | 按核对维度取数 | bpchar | 1 |  | √ | '0' | 按核对维度取数 |
| 4 | fmaintype | 主附表类型 | bpchar | 1 |  | √ | '0' | 主附表类型,枚举: 0 :主表 1 :附表 |
| 5 | fdiffdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fneedmerge | 合并处理 | bpchar | 1 |  | √ | '0' | 合并处理 |
| 11 | fcondition | 生效条件 | varchar | 2000 |  | √ | ' ' | 生效条件 |
| 12 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 13 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fdiffallocate | 差异分配 | bpchar | 1 |  | √ | ' ' | 差异分配,枚举: 1 :首行 2 :末行 3 :平均 4 :金额最大 5 :金额最小 6 :报表项目 |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fisscope | 指定范围 | bpchar | 1 |  | √ | '0' | 指定范围 |
| 18 | fdeffmode | 差异处理 | bpchar | 1 |  | √ | ' ' | 差异处理,枚举: 1 :取大 2 :取小 3 :取借方 4 :取贷方 5 :取平均 6 :取零 7 :手工确认 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 21 | felimtype | 抵销类型 | int8 | 64 |  | √ | 0 | [抵销类型 xkcr_eliminationtype](../xkcr_files/xkcr_eliminationtype.md) |
| 22 | ftranstype | 交易类型 | int8 | 64 |  | √ | 0 | [交易类型 xkcr_transactiontype](../xkcr_files/xkcr_transactiontype.md) |
| 23 | fitem | 报表项目 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_elimentry_gid |  | fgroupid |
| 2 | pk_xkcr_elimtemp |  | fid |
| 3 | idx_xkcr_elimentry_num |  | fnumber |
