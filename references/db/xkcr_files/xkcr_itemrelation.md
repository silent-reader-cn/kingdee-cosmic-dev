# 项目勾稽关系-xkcr_itemrelation

## 分配信息-子表 t_xkrpt_itemrelaallocinfo

- **表名称：** 分配信息-子表
- **表名：** t_xkrpt_itemrelaallocinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftemplateid | 报表模板编码 | varchar | 36 |  | √ | ' ' | [合并报表模板基础 xkcr_rptsamplebase](../xkcr_files/xkcr_rptsamplebase.md) |
| 3 | fsubmitcontrolstrength | 提交控制强度 | bpchar | 1 |  | √ | ' ' | 提交控制强度,枚举: 0 :不检查 1 :仅提示可提交 2 :不可提交 |
| 4 | freportcontrolstrength | 上报控制强度 | bpchar | 1 |  | √ | '0' | 上报控制强度,枚举: 0 :不检查 1 :仅提示可上报 2 :不可上报 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fauditcontrolstrength | 审核控制强度 | bpchar | 1 |  | √ | ' ' | 审核控制强度,枚举: 0 :不检查 1 :仅提示可审核 2 :不可审核 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_itemrelallocinfo_id |  | fid |
| 2 | pk_xkrpt_itemrelaallocinfo |  | fentryid |

---

## 项目勾稽关系-多语言表 t_xkrpt_itemrelation_l

- **表名称：** 项目勾稽关系-多语言表
- **表名：** t_xkrpt_itemrelation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fpromptmsg | 检查不通过时提示内容 | varchar | 255 |  | √ | ' ' | 检查不通过时提示内容 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_itemrelation_l |  | fpkid |
| 2 | idx_xkrpt_itemrelation_l |  | fid,flocaleid |

---

## 项目勾稽关系-主表 t_xkrpt_itemrelation

- **表名称：** 项目勾稽关系-主表
- **表名：** t_xkrpt_itemrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frexpress | 右等式 | varchar | 2000 |  | √ | ' ' | 右等式 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fapplication | 所属应用 | bpchar | 1 |  | √ | '0' | 所属应用,枚举: 0 :xkrpt 1 :xkcr 2 :xkfsa |
| 6 | famountunit | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | frelationoperator | 等式关系 | bpchar | 1 |  | √ | ' ' | 等式关系,枚举: 0 := 1 :> 2 :< 3 :>= 4 :<= 5 :<> |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ferrorrange | 允许误差 | numeric | 23 | 4 | √ | 0 | 允许误差 |
| 14 | flexpress | 左等式 | varchar | 2000 |  | √ | ' ' | 左等式 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fpromptmsg | 检查不通过时提示内容 | varchar | 255 |  | √ | ' ' | 检查不通过时提示内容 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 19 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 20 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_itemrelation |  | fid |
| 2 | idx_xkrpt_itemrelation_num |  | fnumber |
