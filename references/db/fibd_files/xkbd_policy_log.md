# 资产政策更新日志-xkbd_policy_log

## 单据体-子表 t_xkbd_policy_entry_log

- **表名称：** 单据体-子表
- **表名：** t_xkbd_policy_entry_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdecpolicybefore | 减值政策(修改前) | varchar | 50 |  | √ | ' ' | 减值政策(修改前),枚举: 1 :不减值 2 :减值，可转回（限额：累计减值） 4 :减值，可转回（限额：账面价值） 3 :减值，不可转回 |
| 3 | fdepreeffectafter | 变动影响(修改后) | varchar | 50 |  | √ | ' ' | 变动影响(修改后),枚举: NEXT :影响下期 CUR :影响当期 |
| 4 | fassetcatid | 资产类别 | int8 | 64 |  | √ | null | 资产类别 fa_assetcategory |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fnodepreafter | 不提折旧(修改后) | varchar | 50 |  | √ | '0' | 不提折旧(修改后) |
| 8 | fdepretimebefore | 计提时点(修改前) | varchar | 50 |  | √ | ' ' | 计提时点(修改前),枚举: CLEAR :次月 NEW :当月 NEXT_DAY :次日 NEW_AND_CLEAR :当日 NEXT_YEAR :次年 THIS_YEAR :当年 FIRST_YEAR_CONVEN :首年常规 |
| 9 | fdecpolicyafter | 减值政策(修改后) | varchar | 50 |  | √ | ' ' | 减值政策(修改后),枚举: 1 :不减值 2 :减值，可转回（限额：累计减值） 4 :减值，可转回（限额：账面价值） 3 :减值，不可转回 |
| 10 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreater | fcreater | int8 | 64 |  | √ | 0 |  |
| 13 | fdepreeffectbefore | 变动影响(修改前) | varchar | 50 |  | √ | ' ' | 变动影响(修改前),枚举: NEXT :影响下期 CUR :影响当期 |
| 14 | fdepretimeafter | 计提时点(修改后) | varchar | 50 |  | √ | ' ' | 计提时点(修改后),枚举: CLEAR :次月 NEW :当月 NEXT_DAY :次日 NEW_AND_CLEAR :当日 NEXT_YEAR :次年 THIS_YEAR :当年 FIRST_YEAR_CONVEN :首年常规 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fnodeprebefore | 不提折旧(修改前) | varchar | 50 |  | √ | '0' | 不提折旧(修改前) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbd_policy_entry_log |  | fentryid |

---

## 资产政策更新日志-主表 t_xkbd_policy_log

- **表名称：** 资产政策更新日志-主表
- **表名：** t_xkbd_policy_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fpolicyid | 会计政策 | int8 | 64 |  | √ | null | 会计政策 xkbd_policy |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbd_policy_log |  | fid |
