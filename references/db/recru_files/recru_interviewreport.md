# 面试报告-recru_interviewreport

## 候选人不足-子表 t_recru_weaknessentry

- **表名称：** 候选人不足-子表
- **表名：** t_recru_weaknessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweaknesstitle | 不足标题 | varchar | 255 |  | √ | ' ' | 不足标题 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fweaknesscontent | 不足内容 | varchar | 2000 |  | √ | ' ' | 不足内容 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_weaknessentry |  | fentryid |
| 2 | idx_recru_weaknessentry_fid |  | fid |

---

## 面试报告-多语言表 t_recru_interviewreport_l

- **表名称：** 面试报告-多语言表
- **表名：** t_recru_interviewreport_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_interviewreport_l |  | fpkid |
| 2 | idx_recru_interviewreport_l |  | fid,flocaleid |

---

## 面试标签-子表 t_recru_intvlabelentry

- **表名称：** 面试标签-子表
- **表名：** t_recru_intvlabelentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finterviewlabel | 面试标签 | varchar | 255 |  | √ | ' ' | 面试标签 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_intvlabelentry |  | fentryid |
| 2 | idx_recru_intvlabelentry_fid |  | fid |

---

## 面试报告-主表 t_recru_interviewreport

- **表名称：** 面试报告-主表
- **表名：** t_recru_interviewreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finterviewid | 面试管理 | int8 | 64 |  | √ | 0 | [AI面试管理 recru_ai_interview](../recru_files/recru_ai_interview.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | varchar | 50 |  | √ | ' ' | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fksaeanalysis_tag | KSAE模型分析_详情 | text | 0 |  |  | null | KSAE模型分析_详情 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | varchar | 50 |  | √ | ' ' | 主数据内码 |
| 11 | fmatchdegree | 整体匹配度 | numeric | 19 | 6 | √ | 0 | 整体匹配度 |
| 12 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fksaeanalysis | KSAE模型分析 | varchar | 255 |  | √ | ' ' | KSAE模型分析 |
| 14 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 15 | fsummary | 面试总结 | varchar | 2000 |  | √ | ' ' | 面试总结 |
| 16 | fvideourl | 面试视频路径 | varchar | 500 |  | √ | ' ' | 面试视频路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_intereport_number |  | fnumber |
| 2 | pk_recru_interviewreport |  | fid |

---

## 候选人优势-子表 t_recru_strengthentry

- **表名称：** 候选人优势-子表
- **表名：** t_recru_strengthentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstrengthcontent | 优势内容 | varchar | 2000 |  | √ | ' ' | 优势内容 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fstrengthtitle | 优势标题 | varchar | 255 |  | √ | ' ' | 优势标题 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_strengthentry |  | fentryid |
| 2 | idx_recru_strengthentry_fid |  | fid |
