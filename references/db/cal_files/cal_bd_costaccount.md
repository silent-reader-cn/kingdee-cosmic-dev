# 成本主体-cal_bd_costaccount

## 成本主体-多语言表 t_cal_costaccount_l

- **表名称：** 成本主体-多语言表
- **表名：** t_cal_costaccount_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costaccount_l |  | fid,flocaleid |
| 2 | t_cal_costaccount_l_pkey |  | fpkid |

---

## 成本主体-主表 t_cal_costaccount

- **表名称：** 成本主体-主表
- **表名：** t_cal_costaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcalsystemid | 核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 7 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fismainaccount | 是否默认成本主体 | bpchar | 1 |  | √ | '0' | 是否默认成本主体 |
| 9 | fremark_tag | fremark_tag | text | 0 |  |  | null |  |
| 10 | fdividebasisid | 划分依据 | int8 | 64 |  | √ | 0 | 划分依据 cal_bd_dividebasis |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 cal_bd_calpolicy |
| 14 | fbooktypeid | 主体类别 | int8 | 64 |  | √ | 0 | 成本主体类别 cal_bd_costaccounttype |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 18 | fendinitcheck | 结束初始化对账是否提示 | bpchar | 1 |  | √ | '0' | 结束初始化对账是否提示,枚举: A :校验-提示 B :不校验 C :校验-强制 |
| 19 | fisenabledrealtimecost | 启用即时成本 | bpchar | 1 |  | √ | '0' | 启用即时成本 |
| 20 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fenablestandardcost | 启用标准成本 | bpchar | 1 |  | √ | '0' | 启用标准成本 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fendaccountcheck | 结账对账是否提示 | bpchar | 1 |  | √ | '0' | 结账对账是否提示,枚举: A :校验-提示 B :不校验 C :校验-强制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcal_costaccount_ud |  | fcalsystemid,fcalorgid,fcalpolicyid |
| 2 | idx_cal_costacc_calorg |  | fcalorgid |
| 3 | t_cal_costaccount_pkey |  | fid |
