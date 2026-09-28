# 记账模型生成报告-aibkp_accmodgenrep

## 记账模型生成报告-主表 t_aibkp_accmodgenrep

- **表名称：** 记账模型生成报告-主表
- **表名：** t_aibkp_accmodgenrep

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftemnumber | 凭证模板编码 | varchar | 50 |  | √ | ' ' | 凭证模板编码 |
| 5 | fbillstatus | 报告状态 | varchar | 50 |  | √ | ' ' | 报告状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | faccounttable | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 8 | fgentasktag | 任务标识 | varchar | 50 |  | √ | ' ' | 任务标识 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fdetail_tag | 详细信息_详情 | text | 0 |  |  | null | 详细信息_详情 |
| 11 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | faimodel | AI记账模型 | varchar | 50 |  |  | ' ' | AI记账模型 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdetail | 详细信息 | varchar | 2000 |  | √ | ' ' | 详细信息 |
| 15 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbizinfoscheme | 会计事项 | int8 | 64 |  | √ | 0 | [会计事项 ai_bizinfoscheme](../ai_files/ai_bizinfoscheme.md) |
| 17 | fgenstate | 生成情况 | varchar | 50 |  | √ | ' ' | 生成情况,枚举: 0 :成功 1 :错误 |
| 18 | ftemname | 凭证模板名称 | varchar | 255 |  | √ | ' ' | 凭证模板名称 |
| 19 | fruledescription | 记账场景描述 | varchar | 500 |  | √ | ' ' | 记账场景描述 |
| 20 | fmatvoutemp | 匹配到凭证模板 | varchar | 50 |  | √ | ' ' | 匹配到凭证模板,枚举: 0 :是 1 :否 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aibkp_accmodgenrep |  | fid |
| 2 | idx_aibkp_accmodgenrep_m0 |  | fbillno |

---

## 适用账簿-多选基础资料表 t_aibkp_rep_books

- **表名称：** 适用账簿-多选基础资料表
- **表名：** t_aibkp_rep_books

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aibkp_rep_books_fk |  | fid |
| 2 | pk_aibkp_rep_books |  | fpkid |

---

## 记账模型生成报告-多语言表 t_aibkp_accmodgenrep_l

- **表名称：** 记账模型生成报告-多语言表
- **表名：** t_aibkp_accmodgenrep_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | ftemname | 凭证模板名称 | varchar | 500 |  | √ | ' ' | 凭证模板名称 |
| 4 | fruledescription | 记账场景描述 | varchar | 1000 |  | √ | ' ' | 记账场景描述 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aibkp_accmodgenrep_l_0 |  | fid,flocaleid |
| 2 | pk_aibkp_accmodgenrep_l |  | fpkid |
