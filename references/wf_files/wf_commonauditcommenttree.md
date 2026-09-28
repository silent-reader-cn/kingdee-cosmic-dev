# 常用审批意见-wf_commonauditcommenttree

## 常用审批意见-多语言表 t_wf_comauditcomment_l

- **表名称：** 常用审批意见-多语言表
- **表名：** t_wf_comauditcomment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 审批意见 | varchar | 500 |  | √ | ' ' | 审批意见 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_comauditcomment_l_pkey |  | fpkid |
| 2 | idx_wf_comauditcomment_l |  | fid,flocaleid |

---

## 常用审批意见-主表 t_wf_comauditcomment

- **表名称：** 常用审批意见-主表
- **表名：** t_wf_comauditcomment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 审批意见 | varchar | 500 |  | √ | ' ' | 审批意见 |
| 5 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 常用审批意见分组 wf_auditcommentgroup |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 11 | fdecisiontype | 决策类型 | varchar | 30 |  | √ | 'approve' | 决策类型,枚举: approve :同意 reject :驳回 terminate :终止 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_comauditcomment_pkey |  | fid |
| 2 | idx_wf_comauditcomment |  | fnumber |
