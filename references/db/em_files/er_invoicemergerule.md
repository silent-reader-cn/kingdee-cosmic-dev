# 发票合并规则-er_invoicemergerule

## 发票合并规则-多语言表 t_er_invoicemergerule_l

- **表名称：** 发票合并规则-多语言表
- **表名：** t_er_invoicemergerule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_invoicemergerule_l_pkey |  | fpkid |
| 2 | idx_invoicemergerule_l_fid |  | fid |

---

## 发票合并规则-主表 t_er_invoicemergerule

- **表名称：** 发票合并规则-主表
- **表名：** t_er_invoicemergerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmergetype | 合并方式 | varchar | 30 |  | √ | ' ' | 合并方式,枚举: 1 :不合并 2 :同一发票合并 3 :跨发票合并 |
| 3 | fpassengerequal | 旅客相同 | bpchar | 1 |  | √ | '0' | 旅客相同 |
| 4 | ffromequal | 出发地相同 | bpchar | 1 |  | √ | '0' | 出发地相同 |
| 5 | finvoicedateequal | 年月相同 | bpchar | 1 |  | √ | '0' | 年月相同 |
| 6 | ftoequal | 目的地相同 | bpchar | 1 |  | √ | '0' | 目的地相同 |
| 7 | fuserdefinerule | 自定义条件json | varchar | 2000 |  | √ | ' ' | 自定义条件json |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fgoodnameequal | 商品名称相同 | bpchar | 1 |  | √ | '0' | 商品名称相同 |
| 13 | fudrdisplay | 自定义 | varchar | 2000 |  | √ | ' ' | 自定义 |
| 14 | finvoicedatedetailequal | 年月日相同 | bpchar | 1 |  | √ | '0' | 年月日相同 |
| 15 | famountequal | 金额相同 | bpchar | 1 |  | √ | '0' | 金额相同 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fbuyernameequal | 收票公司相同 | bpchar | 1 |  | √ | '0' | 收票公司相同 |
| 19 | fseatgradequal | 座位等级相同 | bpchar | 1 |  | √ | '0' | 座位等级相同 |
| 20 | ftaxrateequal | 税率相同 | bpchar | 1 |  | √ | '0' | 税率相同 |
| 21 | fitemequal | 费用/差旅项目相同 | bpchar | 1 |  | √ | '0' | 费用/差旅项目相同 |
| 22 | fjs | js文本 | varchar | 2000 |  | √ | ' ' | js文本 |
| 23 | foffsetequal | 是否抵扣相同 | bpchar | 1 |  | √ | '1' | 是否抵扣相同 |
| 24 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 |
| 25 | fsalernameequal | 开票公司相同 | bpchar | 1 |  | √ | '0' | 开票公司相同 |
| 26 | forder | 排序序号 | int8 | 64 |  | √ | 0 | 排序序号 |
| 27 | fgoodcodeequal | 税收分类编码相同 | bpchar | 1 |  | √ | '0' | 税收分类编码相同 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fismerge | 是否合并(废弃) | bpchar | 1 |  | √ | '1' | 是否合并(废弃),枚举: 1 :是 0 :否 |
| 31 | ftaxnumequal | 税号相同 | bpchar | 1 |  | √ | '0' | 税号相同 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invoicemerge_invoicetype |  | finvoicetype |
| 2 | t_er_invoicemergerule_pkey |  | fid |
