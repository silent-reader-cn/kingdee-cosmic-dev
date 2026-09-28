# 任务节点编排-recru_agenttask

## 任务节点编排-主表 t_recru_agenttask

- **表名称：** 任务节点编排-主表
- **表名：** t_recru_agenttask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fnodetype | 节点类型 | varchar | 3 |  | √ | ' ' | 节点类型,枚举: A :澄清招聘需求 B :todo_list C :绘制职位画像 D :撰写招聘JD E :选择渠道 F :发布广告与搜寻简历 H :初筛甄选简历 I :邀约AI面试 J :确认邀约 K :推荐最优候选人 L :结束招聘任务 M :总结招聘报告 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | findex | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 7 | fskilltype | 技能类型 | varchar | 50 |  | √ | ' ' | 技能类型,枚举: process :任务流 |
| 8 | fthink | 思考过程 | varchar | 255 |  | √ | ' ' | 思考过程 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 3 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ftype | 任务类型 | varchar | 3 |  | √ | ' ' | 任务类型,枚举: 1 :任务流 2 :脚本执行 3 :文本 |
| 14 | fthink_tag | 思考过程_详情 | text | 0 |  |  | null | 思考过程_详情 |
| 15 | fskillnumber | 技能编码 | varchar | 100 |  | √ | ' ' | 技能编码 |
| 16 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fautocommit | 自动确认 | bpchar | 1 |  | √ | '0' | 自动确认 |
| 19 | fnumber | 节点编码 | varchar | 30 |  | √ | ' ' | 节点编码 |
| 20 | fassistantnumber | 助手编码 | varchar | 50 |  | √ | ' ' | 助手编码 |
| 21 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_agenttask |  | fid |
| 2 | idx_recru_agenttask_index |  | findex |

---

## 任务节点编排-多语言表 t_recru_agenttask_l

- **表名称：** 任务节点编排-多语言表
- **表名：** t_recru_agenttask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_agenttask_l_fid |  | fid,flocaleid |
| 2 | pk_recru_agenttask_l |  | fpkid |
