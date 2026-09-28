# 历史情况反馈-wf_hifeedback

## 历史情况反馈-多语言表 t_wf_hifeedback_l

- **表名称：** 历史情况反馈-多语言表
- **表名：** t_wf_hifeedback_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffeedbackmsg | 反馈意见 | text | 0 |  |  | null | 反馈意见 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hifeedback_l_pkey |  | fpkid |
| 2 | idx_wf_hifeedback_l |  | fid,flocaleid |

---

## 历史情况反馈-主表 t_wf_hifeedback

- **表名称：** 历史情况反馈-主表
- **表名：** t_wf_hifeedback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffeedbackattach | 反馈附件 | varchar | 255 |  | √ | ' ' | 反馈附件 |
| 3 | fmodifierid | 修改人ID | int8 | 64 |  | √ | 0 | 修改人ID |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ffeedbackmsg | 反馈意见 | text | 0 |  |  | null | 反馈意见 |
| 6 | fcreatorid | 创建人id | int8 | 64 |  | √ | 0 | 创建人id |
| 7 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbusinesskey | 业务主键 | varchar | 50 |  | √ | ' ' | 业务主键 |
| 9 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 10 | ffeedbackimg | 反馈图片 | varchar | 255 |  | √ | ' ' | 反馈图片 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hifeedback_busikey |  | fbusinesskey |
| 2 | t_wf_hifeedback_pkey |  | fid |
| 3 | idx_wf_hifeedback_proc |  | fprocinstid |
