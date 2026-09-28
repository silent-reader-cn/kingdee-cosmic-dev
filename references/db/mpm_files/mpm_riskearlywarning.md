# 风险管理-mpm_riskearlywarning

## 风险管理-主表 t_mpm_riskearlywarning

- **表名称：** 风险管理-主表
- **表名：** t_mpm_riskearlywarning

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 风险名称 | varchar | 255 |  | √ | ' ' | 风险名称 |
| 4 | fprojectid | 关联项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fbillstatus | 风险状态 | bpchar | 1 |  | √ | ' ' | 风险状态,枚举: A :未指派 B :待接收 C :跟进中 D :关闭 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fpriority | 优先级 | bpchar | 1 |  | √ | ' ' | 优先级,枚举: 1 :特高 2 :高 3 :中 4 :低 |
| 9 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 10 | fplanclosedate | 预期关闭日期 | timestamp | 0 |  |  | null | 预期关闭日期 |
| 11 | fauditdate | 接收日期 | timestamp | 0 |  |  | null | 接收日期 |
| 12 | fprocessor | 应对人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcloser | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fprocessstrategy | 应对策略 | bpchar | 1 |  | √ | ' ' | 应对策略,枚举: 0 :风险规避 1 :风险缓解 2 :风险转移 3 :风险接受 |
| 17 | fprocessresult | 风险处理判定 | bpchar | 1 |  | √ | ' ' | 风险处理判定,枚举: 0 :已解决 1 :不处理 2 :失控 |
| 18 | fbillstatusbak | 关闭前风险状态 | bpchar | 1 |  | √ | ' ' | 关闭前风险状态,枚举: A :未指派 B :待接收 C :跟进中 D :关闭 |
| 19 | frisktypeid | 风险类型 | int8 | 64 |  | √ | 0 | [风险类型 mpm_risktype](../mpm_files/mpm_risktype.md) |
| 20 | ftaskid | 关联任务 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 21 | fbillno | 风险编码 | varchar | 50 |  | √ | ' ' | 风险编码 |
| 22 | fauditorid | 接收人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_riskearlywarning |  | fbillstatus,fprojectid |
| 2 | pk_mpm_riskearlywarning |  | fid |

---

## 风险管理-分表 t_mpm_riskearlywarning_a

- **表名称：** 风险管理-分表
- **表名：** t_mpm_riskearlywarning_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcloseremark_tag | 风险关闭说明_详情 | text | 0 |  |  | '' | 风险关闭说明_详情 |
| 3 | fcloseremark | 风险关闭说明 | varchar | 255 |  | √ | ' ' | 风险关闭说明 |
| 4 | fdescription | 风险描述 | text | 0 |  |  | '' | 风险描述 |
| 5 | fprocessmethod | 风险应对措施 | text | 0 |  |  | '' | 风险应对措施 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_riskearlywarning_a |  | fid |
| 2 | idx_mpm_riskearlywarning_a |  | fcloseremark |

---

## 风险管理-多语言表 t_mpm_riskearlywarning_l

- **表名称：** 风险管理-多语言表
- **表名：** t_mpm_riskearlywarning_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 风险名称 | varchar | 255 |  | √ | ' ' | 风险名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_riskearlywarning_l |  | fpkid |
