# 用户自定义常用审批意见-wf_usapprovalcomm

## 用户自定义常用审批意见-主表 t_wf_usapprovalcomm

- **表名称：** 用户自定义常用审批意见-主表
- **表名：** t_wf_usapprovalcomm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fseqnum | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 3 | fcomment | 审批意见 | varchar | 1000 |  | √ | ' ' | 审批意见 |
| 4 | fcreateid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fdecisiontype | 决策类型 | varchar | 10 |  | √ | ' ' | 决策类型,枚举: approve :同意 reject :驳回 terminate :终止 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_usapprovalcomm_query |  | fcreateid,fdecisiontype |
| 2 | pk_wf_usapprovalcomm |  | fid |

---

## 用户自定义常用审批意见-多语言表 t_wf_usapprovalcomm_l

- **表名称：** 用户自定义常用审批意见-多语言表
- **表名：** t_wf_usapprovalcomm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 审批意见 | varchar | 1000 |  | √ | ' ' | 审批意见 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_usapprovalcomm_l_query |  | fid,flocaleid |
| 2 | pk_wf_usapprovalcomm_l |  | fpkid |
